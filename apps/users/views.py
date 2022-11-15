from django.conf.global_settings import DEFAULT_FROM_EMAIL
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_str, force_bytes
from rest_framework import status
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
from django.contrib.auth import login
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from users.utils.tokens import account_activation_token


class ActivateUserApiView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({'message': 'User is activated'})
        # else:
            # invalid link
            # return Response({'message': 'invalid link'}, 404)
        return Response({'message': 'invalid link'}, status.HTTP_404_NOT_FOUND)
            # return render(request, 'registration/invalid.html')


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserCreateApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateModelSerializer

    def create(self, request, *args, **kwargs):
        created = super().create(request, *args, **kwargs)
        user = User.objects.get(id=created.data['id'])
        message = render_to_string('activation.html', {
            'username': user.username,
            'domain': get_current_site(request),
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        send_mail('Activation Link', message, EMAIL_HOST_USER, [created.data['email']])
        return Response({'message': 'Check your email'}, status.HTTP_201_CREATED)


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
