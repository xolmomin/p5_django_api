from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import ForeignKey, DateTimeField, \
    CASCADE, SmallIntegerField, Model, CharField, BooleanField, TextField, PositiveIntegerField


class Profile(Model):
    name = CharField(max_length=255)


class Blog(Model):
    name = CharField(max_length=255)


class Lesson(Model):
    name = CharField(max_length=255)


class EduCenter(Model):
    name = CharField(max_length=255)

    class Meta:
        db_table = 'edu_center'


class Task(Model):
    name = CharField(max_length=255)
    is_done = BooleanField(default=False)


class Comment(Model):
    text = TextField()
    content_type = ForeignKey(ContentType, CASCADE)
    object_id = PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'{self.text} ({self.content_type.name})'

#
# class Comment(Model):
#     text = TextField()
#     task = ForeignKey(Task, CASCADE, null=True, blank=True)
#     blog = ForeignKey(Blog, CASCADE, null=True, blank=True)
#     profile = ForeignKey(Profile, CASCADE, null=True, blank=True)
#     lesson = ForeignKey(Lesson, CASCADE, null=True, blank=True)
#     edu_center = ForeignKey(EduCenter, CASCADE, null=True, blank=True)

#
# class TaskComment(Model):
#     text = TextField()
#     task = ForeignKey(Task, CASCADE)
#
#
# class BlogComment(Model):
#     text = TextField()
#     blog = ForeignKey(Blog, CASCADE)
#
#
# class ProfileComment(Model):
#     text = TextField()
#     profile = ForeignKey(Profile, CASCADE)
#


# comment (profile, blog, task)
