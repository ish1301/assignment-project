from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ImageUploadSerializer


class ImageUploadView(APIView):
    parser_classes = [
        FormParser,
        MultiPartParser,
    ]

    def post(self, request):
        serializer = ImageUploadSerializer(data=request.data)

        if serializer.is_valid():
            return Response({"message": "OK"})
        else:
            return Response({"message": "NOPE", "errors": serializer.errors})
