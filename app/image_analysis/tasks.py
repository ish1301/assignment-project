from celery import shared_task

from .models import ImageUpload


@shared_task
def submit_image_analysis(filename, md5_hash):
    return ImageUpload.objects.create(filename=filename, md5_hash=md5_hash)
