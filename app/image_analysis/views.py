from rest_framework.views import APIView

from app.image_analysis.serializers import ImageUploadSerializer


class ImageUploadView(APIView):
    def post(self, request):
        serializer = ImageUploadSerializer(data=request.data)

        if serializer.is_valid():
            return 'OK'
        else:
            return 'NOT_OK'
