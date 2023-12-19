from django.urls import path

from app.image_analysis.views import ImageUploadView

urlpatterns = [
    path('analyze-image/', ImageUploadView.as_view(), name='analyze_image'),
]
