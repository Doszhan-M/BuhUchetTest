from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView, LogoutAPIView, PasswordResetApiView

app_name = 'accounts'

urlpatterns = [
    path('users/signup/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('user/', UserRetrieveUpdateAPIView.as_view()),
    path('user/logout/', LogoutAPIView.as_view()),
    path('user/pass_reset/', PasswordResetApiView.as_view()),
]
