"""
https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html
&
https://testdriven.io/courses/django-celery/getting-started/
"""
import os

from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' app.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_queues.settings")

# register app
app = Celery("dj_queues")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# autodiscover tasks.py from from all registered Django apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task
def divide(x, y):
    import time

    time.sleep(3)
    return x / y
