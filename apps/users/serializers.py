from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.users.models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data['data'] = GetMeModelSerializer(self.user).data
        return data


class UserCreateModelSerializer(ModelSerializer):
    password = CharField(max_length=255, write_only=True)
    confirm_password = CharField(max_length=255, write_only=True)

    def validate(self, attrs):
        confirm_password = attrs.pop('confirm_password')
        password = attrs.get('password')
        if confirm_password != password:
            raise ValidationError("Password didn't match")
        attrs['password'] = make_password(password)
        validated_data = super().validate(attrs)
        return validated_data

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone', 'password', 'confirm_password')
        # extra_kwargs = {
        #     'password': {'write_only': True},
        #     'confirm_password': {'write_only': True},
        # }


class GetMeModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone')


class ForgetPasswordSerializer(Serializer):
    username = CharField(max_length=255)

    def validate_username(self, username):
        if not User.objects.filter(username=username).exists():
            raise ValidationError("Username doesn't exists")
        return username


class ChangePasswordSerializer(Serializer):
    token = CharField(max_length=255)
    password = CharField(max_length=255)
    confirm_password = CharField(max_length=255)

    # def validate_username(self, username):
    #     if not User.objects.filter(username=username).exists():
    #         raise ValidationError("Username doesn't exists")
    #     return username

