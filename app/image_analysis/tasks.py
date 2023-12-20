from celery import shared_task
from decouple import config
from google.cloud import vision

from .models import ImageUpload


@shared_task
def submit_image_analysis(filename, md5_hash, content):
    image = ImageUpload.objects.create(filename=filename, md5_hash=md5_hash)

    client = vision.ImageAnnotatorClient(
        client_options={
            "api_key": config("GOOGLE_API_KEY"),
        }
    )
    req = {
        "image": {"content": content},
        "features": [
            {"type": vision.Feature.Type.LABEL_DETECTION},
            {"type": vision.Feature.Type.IMAGE_PROPERTIES},
        ],
    }

    response = client.annotate_image(request=req)

    print(response)
