from rest_framework.serializers import ImageField, Serializer


class ImageUploadSerializer(Serializer):
    image = ImageField()

