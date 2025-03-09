from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'water.settings')

app = Celery('water')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.broker_connection_retry_on_startup = True

app.conf.update(
    task_track_started=True,
    CELERY_BROKER_URL='redis://localhost:6379/0',
)

app.autodiscover_tasks()
