from time import sleep
from celery import shared_task

from .models import File


@shared_task()
def process_file(id_file):
    sleep(10)  # Для того, чтобы увидеть асинхронную работу
    File.objects.filter(id=id_file).update(processed=True)
