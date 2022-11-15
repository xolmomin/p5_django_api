from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, GenericAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from orders.models import Product, Category
from orders.serializers import ProductModelSerializer, CategoryModelSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.order_by('-created_at')
    serializer_class = ProductModelSerializer
    filter_backends = (DjangoFilterBackend,)
    # search_fields = '__all__'
    # ordering_fields = ('id', 'name', 'price')
    filterset_fields = ('name', 'price_gte')

    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'message': 'Successfully created!'}, status=status.HTTP_201_CREATED, headers=headers)


# CRUD
class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = (IsAuthenticated,)


'''
http://localhost:8000/api/v1/orders/product/?search=90000
http://localhost:8000/api/v1/orders/product/?name=nok&price=9000
http://localhost:8000/api/v1/orders/product/?name=nok&search=9000

'''
