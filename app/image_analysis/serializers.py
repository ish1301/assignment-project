from rest_framework.serializers import ImageField, ModelSerializer, ValidationError

from .models import MAX_IMAGE_SIZE, ImageUpload


class ImageUploadSerializer(ModelSerializer):
    image = ImageField()

    class Meta:
        model = ImageUpload
        fields = "__all__"

    def validate_image(self, file):
        if file.size > MAX_IMAGE_SIZE:
            raise ValidationError(
                f"File size exceeds the allowed limit ({MAX_IMAGE_SIZE} bytes)."
            )

        return file
