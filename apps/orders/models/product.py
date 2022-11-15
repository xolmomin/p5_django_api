from ckeditor.fields import RichTextField
from django.db.models import ForeignKey, DecimalField, DateTimeField, \
    CASCADE, JSONField, SET_NULL, SmallIntegerField
from django.utils.text import slugify

from shared.django import SlugBaseModel


class Product(SlugBaseModel):
    description = RichTextField()
    price = DecimalField(decimal_places=2, max_digits=9)
    category = ForeignKey('orders.Category', CASCADE)
    spec = JSONField(default=dict, null=True, blank=True)
    discount = SmallIntegerField(default=0)
    quantity = SmallIntegerField(default=1)
    shipping_cost = SmallIntegerField(default=0)

    updated_by = ForeignKey('users.User', SET_NULL, null=True, blank=True)
    created_by = ForeignKey('users.User', SET_NULL, 'products', null=True, blank=True)

    updated_at = DateTimeField(auto_now=True)
    created_at = DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        while Product.objects.filter(slug=self.slug).exists():
            self.slug += self.slug + '1'
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
