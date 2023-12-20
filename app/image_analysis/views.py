from google.cloud import vision
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .serializers import ImageUploadSerializer

client = vision.ImageAnnotatorClient()


class ImageUploadView(APIView):
    parser_classes = [
        FormParser,
        MultiPartParser,
    ]

    def post(self, request):
        serializer = ImageUploadSerializer(data=request.data)

        if serializer.is_valid():
            return Response(
                {"message": "Image submitted for analysis"}, status=HTTP_200_OK
            )
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
