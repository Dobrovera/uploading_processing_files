import os
from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "uploading_processing.settings")
app = Celery("uploading_processing")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
