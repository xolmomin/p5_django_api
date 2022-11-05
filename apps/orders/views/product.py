from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from orders.models import Product, Category
from orders.serializers import ProductModelSerializer, CategoryModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.order_by('-created_at')
    serializer_class = ProductModelSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = (IsAuthenticated, )
