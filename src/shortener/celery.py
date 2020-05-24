"""
Celery configuration module
"""
from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shortener.settings')

app = Celery('shortener')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    """
    Default celery task used for debugging
    """
    print('Request: {0!r}'.format(self.request))
