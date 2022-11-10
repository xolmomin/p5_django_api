from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from orders.views.product import ProductModelViewSet, CategoryListAPIView

router = DefaultRouter()
router.register('product', ProductModelViewSet, 'product')
# router.register('category', CategoryModelViewSet, 'category')

urlpatterns = [
    path('', include(router.urls)),
    path('category', CategoryListAPIView.as_view(), name='product'),
]
