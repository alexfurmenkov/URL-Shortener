"""
Module with UrlShortenHandler class
to save new short URL to DB
"""
from django.contrib.sessions.models import Session
from rest_framework.response import Response
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema

from shortener.decorators import request_validation
from shortener.models import UrlAddress
from shortener.utils import RedisStorage
from shortener.events import (
    ResponseCreated,
    ResponseSuccess,
    ResponseAlreadyExists,
    ResponseNotFound
)
from shortener.serializers import (
    UrlAddressSerializer,
    UrlShortenSerializer
)

redis_storage = RedisStorage()


class UrlShortenHandler(APIView):
    """
    Class-based view to handle requests on
    "api/short/"
    """

    @classmethod
    @swagger_auto_schema(
        responses={
            '200': 'List of all URLs is returned',
            '404': 'URLs with such session id are not found'
        }
    )
    def get(cls, request) -> Response:
        """
        Returns all URLs of the user according to session key
        :param request: GET HTTP Request on "api/short/"
        :return: JSON Response with URL details
        """
        session = Session.objects.get(session_key=request.session.session_key)
        url_list = redis_storage.get_url_list(session.session_key)

        if url_list is None:
            url_list = UrlAddress.get_objects_by_user_session(session)
            url_list_serializer = UrlAddressSerializer(
                instance=url_list,
                many=True
            )
            redis_storage.save_url_list(
                url_list_serializer.data,
                session.session_key
            )

        if not url_list:
            return ResponseNotFound('You do not have any urls')

        url_list_serializer = UrlAddressSerializer(
            instance=url_list,
            many=True
        )
        return ResponseSuccess(url_list_serializer.data)

    @classmethod
    @request_validation(UrlShortenSerializer)
    @swagger_auto_schema(
        request_body=UrlShortenSerializer(),
        responses={
            '201': 'New short URL is saved',
            '409': 'Such short URL already exists'
        }
    )
    def post(cls, request) -> Response:
        """
        Saves new short URL to DB if it hasn't been saved before
        :param request: POST HTTP Request with URL to shorten
                        in body, e.g. {'URL': 'http://www.vk.com'}
        :return: JSON Response with new short URL details
        """
        session = Session.objects.get(session_key=request.session.session_key)

        new_url_data = request.data.copy()
        new_url_data['user_session'] = session
        new_url = UrlAddress.create_url(new_url_data)

        if new_url is None:
            return ResponseAlreadyExists('Such short URL already exists')

        url_serializer = UrlAddressSerializer(new_url)
        redis_storage.append_url_to_list(
            url_serializer.data,
            session.session_key
        )
        return ResponseCreated(url_serializer.data)
