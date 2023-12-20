import hashlib

from rest_framework.serializers import ImageField, Serializer, ValidationError

from .models import MAX_IMAGE_SIZE
from .tasks import submit_image_analysis


class ImageUploadSerializer(Serializer):
    image = ImageField()

    def validate_image(self, file):
        """
        Validate image size before submitting it to the workers

        Parameters:
            - file (object): The InMemoryUploadedFile of image file.

        Return
            - file (object): For further processing
        """

        if file.size > MAX_IMAGE_SIZE:
            raise ValidationError(
                f"File size exceeds the allowed limit ({MAX_IMAGE_SIZE} bytes)."
            )

        content = file.file.read()
        md5hash = hashlib.md5(content)
        submit_image_analysis.delay(
            filename=file.name, md5_hash=md5hash.hexdigest(), content=content
        )

        return file
