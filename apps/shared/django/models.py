from django.db.models import CharField, SlugField, Model


class SlugBaseModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)

    class Meta:
        abstract = True
