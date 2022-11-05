from django.db.models import ForeignKey, DateTimeField, \
    CASCADE, SmallIntegerField, Model


class UserProductMixin(Model):
    product = ForeignKey('orders.Product', CASCADE)
    author = ForeignKey('users.User', CASCADE)

    class Meta:
        abstract = True


class Cart(UserProductMixin):
    quantity = SmallIntegerField(default=1)
    created_at = DateTimeField(auto_now_add=True)


class Wishlist(UserProductMixin):
    created_at = DateTimeField(auto_now_add=True)
