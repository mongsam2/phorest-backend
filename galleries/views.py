from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from .models import Gallery, Category
from users.models import User

from .serializers import GetGalleriesSerializer
# Create your views here.
class Galleries(APIView):

    def get(self, request):
        category_name = request.query_params.get("category")
        if not category_name:
            raise ParseError("category가 입력되지 않았습니다.")

        try:
            category_id = Category.objects.get(name=category_name)
        except:
            raise ParseError("DB에서 해당 카테고리를 찾을 수 없습니다.")
        
        galleries = Gallery.objects.filter(category=category_id)
        serializer = GetGalleriesSerializer(galleries, many=True)
        
        return Response(serializer.data)

