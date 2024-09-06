from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status
from django.conf import settings

from .models import Gallery, Category, ImageType
from users.models import User
from django.db.models import Count

from .serializers import (
    GetGalleriesSerializer,
    PostGalleriesSerializer,
    GetGalleryRankingSerializer,
)


# Create your views here.
def get_category_id(category_name):
    if not category_name:
        raise ParseError("category가 입력되지 않았습니다.")

    try:
        category_id = Category.objects.get(name=category_name)
    except:
        raise ParseError("DB에서 해당 카테고리를 찾을 수 없습니다.")
    return category_id


class Galleries(APIView):

    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        category_id = get_category_id(request.query_params.get("category"))

        galleries = Gallery.objects.filter(category=category_id)
        serializer = GetGalleriesSerializer(
            galleries,
            many=True,
            context={"request": request},
        )

        return Response(data=serializer.data)

    def post(self, request):
        serializer = PostGalleriesSerializer(data=request.data)
        user = request.user

        if settings.DEBUG and not user.is_authenticated:
            user = User.objects.get(username=settings.SUPERUSER)

        if serializer.is_valid():

            gallery = serializer.save(owner=user)
            return Response(
                data={"detail": "Upload Gallery"}, status=status.HTTP_200_OK
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GalleriesRanking(APIView):

    def get(self, request):
        category_id = get_category_id(request.query_params.get("category"))
        galleries = Gallery.objects.annotate(like_count=Count("like_users")).order_by(
            "-like_count"
        )[:6]
        serializer = GetGalleryRankingSerializer(
            galleries,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)
