from rest_framework.serializers import ModelSerializer

from orders.models import Product, Category


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        exclude = ()


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


