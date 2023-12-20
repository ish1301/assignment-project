from rest_framework.serializers import ImageField, Serializer, ValidationError

from .models import MAX_IMAGE_SIZE


class ImageUploadSerializer(Serializer):
    image = ImageField()

    def validate_image(self, file):
        if file.size > MAX_IMAGE_SIZE:
            raise ValidationError(
                f"File size exceeds the allowed limit ({MAX_IMAGE_SIZE} bytes)."
            )

        return file
