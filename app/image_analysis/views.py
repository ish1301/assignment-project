from drf_spectacular.utils import extend_schema
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .serializers import ImageUploadSerializer


class ImageUploadView(APIView):
    parser_classes = [
        FormParser,
        MultiPartParser,
    ]

    @extend_schema(
        operation_id="POST image for analysis",
        request=ImageUploadSerializer,
        responses=ImageUploadSerializer,
    )
    def post(self, request):
        serializer = ImageUploadSerializer(data=request.data)

        if serializer.is_valid():
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
