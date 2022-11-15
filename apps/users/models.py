from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, BooleanField, EmailField


class User(AbstractUser):
    phone = CharField(max_length=12, unique=True)
    email = EmailField(max_length=255, unique=True)
    is_active = BooleanField(default=False)

    REQUIRED_FIELDS = ['phone', 'email']
