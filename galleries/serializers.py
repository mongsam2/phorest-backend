from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ImageField,
)
from .models import Gallery
from users.models import User
from django.conf import settings


class GetGalleriesSerializer(ModelSerializer):

    background = ImageField(source="background.image", read_only=True)
    profile = ImageField(source="owner.profile_image", read_only=True)
    is_liked = SerializerMethodField()
    like_count = SerializerMethodField()

    class Meta:
        model = Gallery
        fields = (
            "image",
            "title",
            "upload_date",
            "background",
            "profile",
            "is_liked",
            "like_count",
        )

    def get_is_liked(self, obj):
        request = self.context.get("request")
        if not request.user.is_authenticated:
            return False
        liked = obj.like_users.filter(id=request.user.id).exists()
        return liked

    def get_like_count(self, obj):
        total = obj.like_users.all().count()
        return total


class PostGalleriesSerializer(ModelSerializer):

    class Meta:
        model = Gallery
        fields = ("image", "title", "background", "category", "image_type")


class GetGalleryRankingSerializer(ModelSerializer):

    image = ImageField(use_url=True)
    profile = ImageField(source="owner.profile_image", read_only=True)

    class Meta:
        model = Gallery
        fields = ("id", "image", "title", "profile")
