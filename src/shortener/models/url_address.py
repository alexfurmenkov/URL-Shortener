"""
URL Address model
"""
import datetime
import logging
import secrets

from django.db import models
from django.contrib.sessions.models import Session
from django.utils import timezone

error_logger = logging.getLogger('error_logger')
info_logger = logging.getLogger('info_logger')


class UrlAddress(models.Model):
    """
    UrlAddress model
    """

    class Meta:
        app_label = 'shortener'

    user_session = models.ForeignKey(Session, on_delete=models.CASCADE,
                                     default=None)
    original_url = models.CharField(max_length=8192, default=None)
    short_url = models.CharField(max_length=8192, default=None)
    expiry_date = models.DateTimeField(default=None)

    @classmethod
    def create_url(cls, data: dict):
        """
        Creates new UrlAddress object
        :param data: dict with original_url
                    and optionally short_url
        :return: UrlAddress object if created,
                if already exists - returns None
        """
        short_url = None
        if 'short_url' in data:
            data_short_url = data['short_url']
            if cls.get_object_by_short_url(data_short_url) is not None:
                error_logger.error(
                    f'Object of class {cls.__name__} '
                    f'with short URL \"{short_url}\" already exists'
                )
                return None
            short_url = data_short_url
        else:
            random_sequence = secrets.token_urlsafe(6)
            short_url = random_sequence

        new_url = cls.objects.create(
            user_session=data['user_session'],
            original_url=data['original_url'],
            short_url=short_url,
            expiry_date=timezone.now() + datetime.timedelta(days=10)
        )
        info_logger.info(
            f'New {cls.__name__} object {new_url} is created'
        )
        return new_url

    @classmethod
    def get_objects_by_user_session(cls, user_session):
        """
        Gets UrlAddress objects by user session
        :param user_session: session key of current user
        :return: list of UrlAddress objects if they exist,
                 if not - returns None
        """
        urls = cls.objects.filter(user_session=user_session)

        if not urls:
            error_logger.error(
                f'Objects of class {cls.__name__} '
                f'with user session \"{user_session}\" are not found'
            )
        return urls

    @classmethod
    def get_object_by_id(cls, object_id: int):
        """
        Gets UrlAddress object by id
        :param object_id: id of UrlAddress object
        :return: UrlAddress object if it exists,
                 if not - returns None
        """
        try:
            existing_object = cls.objects.get(id=object_id)
            return existing_object
        except cls.DoesNotExist:
            error_logger.error(
                f'Object of class {cls.__name__} '
                f'with id \"{object_id}\" is not found'
            )
            return None

    @classmethod
    def get_object_by_original_url(cls, original_url: str):
        """
        Gets UrlAddress object by original URL
        :param original_url: Original URL of UrlAddress object
        :return: UrlAddress object if it exists,
                         if not - returns None
        """
        try:
            existing_object = cls.objects.get(original_url=original_url)
            return existing_object
        except cls.DoesNotExist:
            error_logger.error(
                f'Object of class {cls.__name__} with '
                f'original url \"{original_url}\" is not found'
            )
            return None

    @classmethod
    def get_object_by_short_url(cls, short_url: str):
        """
        Gets UrlAddress object by short URL
        :param short_url: Short URL of UrlAddress object
        :return: UrlAddress object if it exists,
                         if not - returns None
        """
        try:
            existing_object = cls.objects.get(short_url=short_url)
            return existing_object
        except cls.DoesNotExist:
            error_logger.error(
                f'Object of class {cls.__name__} with '
                f'short url \"{short_url}\" is not found'
            )
            return None
