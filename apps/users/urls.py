from django.urls import path, re_path

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from users.views import UserCreateApiView, GetMeApiView, CustomTokenObtainPairView, ForgetPasswordApiView, \
    ChangePasswordApiView


urlpatterns = [
    path('register/', UserCreateApiView.as_view(), name='register'),
    path('forgot-password/', ForgetPasswordApiView.as_view(), name='forget_password'),  # user
    path('change-password/', ChangePasswordApiView.as_view(), name='change_password'),  # user
    path('forgot-password/<int:pk>', ForgetPasswordApiView.as_view(), name='forget_password_by_id'),  # Moderator
    # re_path(r'^activate_account/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',ActivateAccountView.as_view(), name='activate_account'),
    # path('get-me/', GetMeApiView.as_view(), name='get_me'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
