from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.models import User
from apps.users.serializers import UserCreateModelSerializer
from root.settings import EMAIL_HOST_USER
from users.serializers import GetMeModelSerializer, CustomTokenObtainPairSerializer, ForgetPasswordSerializer, \
    ChangePasswordSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateModelSerializer


class ChangePasswordApiView(GenericAPIView):
    serializer_class = ChangePasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        serializer_data.is_valid(raise_exception=True)

        return Response({'status': 'updated your password'})


class ForgetPasswordApiView(GenericAPIView):
    serializer_class = ForgetPasswordSerializer

    def __send_email_confirmation_token(self, username):
        user = User.objects.filter(username=username).first()
        send_mail('Reset password', 'parolni tiklash uchun linkni bosing', EMAIL_HOST_USER, [user.email])

    def post(self, request, *args, **kwargs):
        serializer_data = self.serializer_class(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        username = serializer_data.data.get('username')
        self.__send_email_confirmation_token(username)
        return Response({'status': 'check your email'})


'''
username
client(Frontend) -> API forgot-password

password
confirm_password
token

 
'''


class GetMeApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None, *args, **kwargs):
        user = request.user
        serializer_data = GetMeModelSerializer(user).data
        return Response(serializer_data)
