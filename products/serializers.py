from rest_framework.serializers import ModelSerializer
from .models import Product


class GetProductsSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ("image", "name", "price")
