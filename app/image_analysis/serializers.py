import magic
from rest_framework.serializers import ImageField, Serializer, ValidationError


class ImageUploadSerializer(Serializer):
    image = ImageField()

    def validate_image(self, value):
        mime = magic.Magic()
        file_mime_type = mime.from_buffer(value.read(1024))

        # Allowed MIME types
        allowed_mime_types = ["image/jpeg", "image/png", "image/gif"]

        # Max file size
        max_file_size = 5 * 1024 * 1024  # 5 MB

        if file_mime_type not in allowed_mime_types:
            raise ValidationError(
                "Invalid file format. Only images (JPEG, PNG, GIF) are allowed."
            )
        if value.size > max_file_size:
            raise ValidationError(
                f"File size exceeds the allowed limit ({max_file_size} bytes)."
            )

        return value
