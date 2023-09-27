from .models import File
from celery import shared_task


@shared_task()
def process_file(file):
    File.objects.filter(file=file).update(processed=True)
