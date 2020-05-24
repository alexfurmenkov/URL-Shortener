"""
Module with celery tasks
"""
from __future__ import absolute_import, unicode_literals

import datetime
import logging

from celery import shared_task

from .models import UrlAddress


info_logger = logging.getLogger('info_logger')


@shared_task
def delete_old_urls():
    """
    Deletes urls that have expired
    """
    print('Starting to check if there are some old urls')
    current_time_date = datetime.datetime.now()

    for url in UrlAddress.objects.all():
        if current_time_date >= url.expiry_date:
            url.delete()
            print(f'Url {url.short_url} is deleted')
            info_logger.info(
                f'Url {url.short_url} is deleted'
            )
