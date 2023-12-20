import json

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

    request = {
        "image": {"content": content},
        "features": [{"type_": vision.Feature.Type.LABEL_DETECTION}],
    }

    response = client.annotate_image(request)
    response_json = vision.AnnotateImageResponse.to_json(response)

    image.analysis = json.dumps(response_json)
    image.save()

    return image
