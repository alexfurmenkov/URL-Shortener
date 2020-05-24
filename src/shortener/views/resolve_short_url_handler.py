"""
Module with ResolveShortUrlHandler class
to redirect user to the original URL
of the short one given in the request
"""
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema

from shortener.models import UrlAddress
from shortener.serializers import UrlAddressSerializer


class ResolveShortUrlHandler(APIView):
    """
    Class-based view to handle requests on
    "/<slug:short_url>/"
    """
    @classmethod
    @swagger_auto_schema(
        responses={
            '201': 'User is redirected to original URL',
            '404': 'Such short URL does not exist'
        }
    )
    def get(cls, request, short_url):
        """
        Redirects user to the original url
        of the short one given in request
        :param short_url: Short URL
        :param request: GET HTTP Request with short URL
        :return: Redirect to the original URL
        """
        existing_url = UrlAddress.get_object_by_short_url(short_url)

        if not existing_url:
            return TemplateResponse(request, 'error.html', status=404)

        url_serializer = UrlAddressSerializer(existing_url)
        redirect_url = url_serializer.data['original_url']
        return redirect(redirect_url)
