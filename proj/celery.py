from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

from celery.schedules import crontab

from datetime import timedelta


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'run_transactions_every_30_seconds': {
        'task': 'task3.tasks.run_transactions',
        'schedule': timedelta(seconds=30),
    },
}

# app.conf.beat_schedule = {
#     'run_transactions_daily_at_3_15_pm': {
#         'task': 'task3.tasks.run_transactions',
#         'schedule': crontab(hour=15, minute=15),
#     },
# }
