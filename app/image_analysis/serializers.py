from rest_framework.serializers import (
    ImageField,
    ModelSerializer,
    Serializer,
    ValidationError,
)

from .models import MAX_IMAGE_SIZE, ImageUpload
from .tasks import submit_image_analysis


class ImageUploadSerializer(Serializer):
    image = ImageField()

    def validate_image(self, file):
        if file.size > MAX_IMAGE_SIZE:
            raise ValidationError(
                f"File size exceeds the allowed limit ({MAX_IMAGE_SIZE} bytes)."
            )

        submit_image_analysis.delay()

        return file


class ImageAnalysisSerializer(ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = ("filename", "md5_hash", "analysis", "uploaded_at")

    def create(self, validated_data):
        image = validated_data["image"]
        validated_data.pop("image", None)

        validated_data["filename"] = image.name
        validated_data["md5_hash"] = image.name

        return super().create(validated_data)
