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
