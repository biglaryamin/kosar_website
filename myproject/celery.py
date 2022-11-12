import os

from celery import Celery  
from celery.schedules import crontab  
from django.conf import settings
  
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
app = Celery("myproject")
app.config_from_object("django.conf:settings", namespace="CELERY")


app.conf.beat_schedule = {
    'print-something': {
    'task': 'crawler.tasks.test_func',
    'schedule': 5.0, # every 5 seconds it will be called
    #'args': (2,) you can pass arguments also if rquired
    },
}

app.autodiscover_tasks()