from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView, LogoutAPIView, PasswordResetApiView

app_name = 'accounts'

urlpatterns = [
    path('users/signup/', RegistrationAPIView.as_view(), name='signup'),
    path('users/login/', LoginAPIView.as_view(), name='login'),
    path('user/', UserRetrieveUpdateAPIView.as_view(), name='user'),
    path('user/logout/', LogoutAPIView.as_view(), name='logout'),
    path('user/pass_reset/', PasswordResetApiView.as_view(), name='pass_reset'),
]
