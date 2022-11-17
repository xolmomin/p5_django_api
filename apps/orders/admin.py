from django.apps import apps
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from django.db.models import QuerySet

from orders.models import Product, Category, Comment, Task, Profile, Blog


class TaskCommentProxy(Comment):
    class Meta:
        proxy = True
        verbose_name = 'Tasklarning kommenti'
        verbose_name_plural = 'Tasklarning kommentlari'


class ProfileCommentProxy(Comment):
    class Meta:
        proxy = True
        verbose_name = 'Profilelarning kommenti'
        verbose_name_plural = 'Profilelarning kommentlari'


class BlogCommentProxy(Comment):
    class Meta:
        proxy = True
        verbose_name = 'Bloglarning kommenti'
        verbose_name_plural = 'Bloglarning kommentlari'


@admin.register(TaskCommentProxy)
class TaskCommentModelAdmin(ModelAdmin):

    def get_queryset(self, request):
        qs: QuerySet = super().get_queryset(request)
        content_type = ContentType.objects.get_for_model(Task)
        return qs.filter(content_type=content_type)


@admin.register(ProfileCommentProxy)
class ProfileCommentModelAdmin(ModelAdmin):
    def get_queryset(self, request):
        qs: QuerySet = super().get_queryset(request)
        content_type = ContentType.objects.get_for_model(Profile)
        return qs.filter(content_type=content_type)


@admin.register(BlogCommentProxy)
class BlogCommentModelAdmin(ModelAdmin):
    def get_queryset(self, request):
        qs: QuerySet = super().get_queryset(request)
        content_type = ContentType.objects.get_for_model(Blog)
        return qs.filter(content_type=content_type)


@admin.register(Comment)
class CommentModelAdmin(ModelAdmin):
    pass

#
#
# @admin.register(Product)
# class ProductAdmin(ModelAdmin):
#     exclude = ('slug',)
#
#
# @admin.register(Category)
# class CategoryAdmin(ModelAdmin):
#     exclude = ('slug',)

admin.site.unregister(Group)
