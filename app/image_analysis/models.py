from django.db import models

MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5MB


class ImageUpload(models.Model):
    # Avoid storing image
    filename = models.CharField(max_length=255, blank=True)
    md5_hash = models.CharField(max_length=32, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
