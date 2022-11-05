from django.contrib import admin
from django.contrib.admin import ModelAdmin

from orders.models import Product, Category


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    exclude = ('slug',)


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    exclude = ('slug',)
