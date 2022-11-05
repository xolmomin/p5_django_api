from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from orders.views.product import ProductModelViewSet, CategoryModelViewSet

router = DefaultRouter()
router.register('product', ProductModelViewSet, 'product')
router.register('category', CategoryModelViewSet, 'category')

urlpatterns = [
    path('', include(router.urls)),
    # path('products', ProductModelViewSet.as_view(), name='product'),
    # path('product/detail/<int:pk>', ProductModelViewSet.as_view(), name='product')
    # path('product/delete/<int:pk>', ProductModelViewSet.as_view(), name='product')
    # path('product/update/<int:pk>', ProductModelViewSet.as_view(), name='product')
]
