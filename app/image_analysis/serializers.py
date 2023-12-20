import hashlib

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

        content = file.file.read()
        md5hash = hashlib.md5(content)
        submit_image_analysis.delay(
            filename=file.name, md5_hash=md5hash.hexdigest(), content=content
        )

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
