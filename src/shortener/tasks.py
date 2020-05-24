"""
Module with celery tasks
"""
from __future__ import absolute_import, unicode_literals

import logging

from celery import shared_task

from django.utils import timezone

from shortener.utils import RedisStorage
from shortener.models import UrlAddress
from shortener.serializers import UrlAddressSerializer


info_logger = logging.getLogger('info_logger')
redis_storage = RedisStorage()


@shared_task
def delete_old_urls():
    """
    Deletes urls that have expired
    """
    print('Starting to check if there are some old urls')
    current_time_date = timezone.now()

    for url in UrlAddress.objects.all():
        if current_time_date >= url.expiry_date:
            url_serializer = UrlAddressSerializer(url)
            url_session_key = url.user_session

            redis_storage.remove_url_from_list(
                url=url_serializer.data,
                session_key=url_session_key
            )
            url.delete()

            print(f'Url {url.short_url} is deleted')
            info_logger.info(
                f'Url {url.short_url} is deleted'
            )
