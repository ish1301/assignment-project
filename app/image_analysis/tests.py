from django.test import TestCase
from rest_framework.status import HTTP_200_OK
from rest_framework.test import APIClient


class ImageUploadViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_image_upload_valid(self):
        """
        Test the image upload view with a valid image.
        """
        file_path = "tests/data/valid-image.jpg"
        with open(file_path, "rb") as image:
            response = self.client.post(
                "/analyze-image/",
                data={"image": image},
                format="multipart",
            )

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, {"message": "Image submitted for analysis"})
