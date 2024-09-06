from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from urllib.parse import quote

from users.models import User
from .models import Gallery, Background, Category, ImageType


# Create your tests here.
class TestGalleries(APITestCase):

    def setUp(self) -> None:
        sample_image = SimpleUploadedFile(
            name="test.png",
            content=b"\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\xff\x00,\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02L\x01\x00;",
            content_type="image/png",
        )
        background = Background.objects.create(image=sample_image)
        category = Category.objects.create(name="동물")
        image_type = ImageType.objects.create(name="사진")
        dumy_user = User.objects.create_user(
            username="testuser", password="testpassword", email="testuser@example.com"
        )
        self.gallery = Gallery.objects.create(
            image=sample_image,
            title="test1",
            background=background,
            category=category,
            image_type=image_type,
            owner=dumy_user,
        )

    def test_get_galleries(self):
        response = self.client.get("/api/galleries/", {"category": "동물"})
        content = response.json()
        status = response.status_code
        self.assertIsInstance(content, list, "응답이 리스트의 형태가 아닙니다.")
