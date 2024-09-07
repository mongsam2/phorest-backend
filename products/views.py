from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, NotFound
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status

from .serializers import GetProductsSerializer
from .models import Product


# Create your views here.
class Products(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = GetProductsSerializer(
            products, many=True, context={"request": request}
        )
        return Response(serializer.data)


class ProductDetail(APIView):

    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise NotFound("해당 제품이 없습니다.")
        serializer = GetProductsSerializer(product, context={"request": request})
        return Response(serializer.data)
