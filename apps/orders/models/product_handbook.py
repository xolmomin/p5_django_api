from django.db.models import Model, CharField, ForeignKey, CASCADE, ImageField, SET_NULL, DateTimeField, \
    TextField, SmallIntegerField, IntegerChoices
from django.utils.text import slugify
from mptt.models import MPTTModel, TreeForeignKey

from shared.django.models import SlugBaseModel


class Category(SlugBaseModel, MPTTModel):
    parent = TreeForeignKey('orders.Category', CASCADE, 'children', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        while Category.objects.filter(slug=self.slug).exists():
            self.slug += self.slug + '1'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    class MPTTMeta:
        order_insertion_by = ['name']


class ProductImages(Model):
    product = ForeignKey('orders.Product', CASCADE)
    image = ImageField(upload_to='products/images/')

#
# class Comment(Model):
#     class Rating(IntegerChoices):
#         EXCELLENT = 5
#         GOOD = 4
#         AVERAGE = 3
#         BAD = 2
#         WORSE = 1
#
#     name = CharField(max_length=255)
#     text = TextField()
#     rate = SmallIntegerField(default=Rating.EXCELLENT, choices=Rating.choices)
#     product = ForeignKey('orders.Product', CASCADE)
#     author = ForeignKey('users.User', SET_NULL, null=True, blank=True)
#     updated_at = DateTimeField(auto_now=True)
#     created_at = DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ['-created_at']
