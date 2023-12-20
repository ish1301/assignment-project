import hashlib

from rest_framework.serializers import (
    ImageField,
    Serializer,
    SerializerMethodField,
    ValidationError,
)

from .models import MAX_IMAGE_SIZE
from .tasks import submit_image_analysis


class ImageUploadSerializer(Serializer):
    image = ImageField()
    message = SerializerMethodField()
    md5_hash = SerializerMethodField()

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

        self.message = "Image submitted for analysis"

        content = file.file.read()
        md5hash = hashlib.md5(content)
        self.md5_hash = md5hash.hexdigest()
        submit_image_analysis.delay(
            filename=file.name, md5_hash=self.md5_hash, content=content
        )

        return file

    def get_message(self, value):
        return self.message

    def get_md5_hash(self, value):
        return self.md5_hash
