from rest_framework.fields import CurrentUserDefault, IntegerField
from rest_framework.serializers import ModelSerializer, HiddenField

from orders.models import Product, Category


class ProductModelSerializer(ModelSerializer):
    # quantity = IntegerField(default=50)
    # shipping_cost = IntegerField(default=150)
    # discount = IntegerField(default=10)
    created_by = HiddenField(default=CurrentUserDefault())
    updated_by = HiddenField(default=CurrentUserDefault())

    # def create(self, validated_data):
        # print(123)
        # validated_data['created_by'] = self.context['request'].user
        # validated_data['updated_by'] = self.context['request'].user
        # return super().create(validated_data)

    # updated_by = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Product
        exclude = ()


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['products'] = ProductModelSerializer(instance.product_set.all(), many=True).data
        return repr




