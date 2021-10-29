from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView, UpdateAPIView, RetrieveAPIView
from django.contrib.auth import logout

from .models import User
from .serializers import RegistrationSerializer, LoginSerializer, UserSerializer
from .tasks import new_password_send_to_email


class RegistrationAPIView(APIView):
    '''Регистрация пользователя.'''
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    '''Авторизация пользователя.'''
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    '''Обновление данных пользователя.'''
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutAPIView(APIView):
    '''Выход пользователя.'''

    def get(self, request, format=None):
        logout(request) # using Django logout
        return Response(status=status.HTTP_200_OK)

from password_generator import PasswordGenerator
class PasswordResetApiView(UpdateAPIView):
    '''Сброс пароля, с отправкой на уведомления по email'''

    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def get_object(self):
        '''Получить обьект.'''
        email = self.request.data['user'].get('email')
        object = User.objects.get(email=email)
        return object

    def update(self, request, *args, **kwargs):
        """обновить пароль и отправить по email"""
        pwo = PasswordGenerator()
        pwo.minlen = 8
        new_password = pwo.generate()
        serializer_data = request.data.get('user', {})
        serializer_data['password'] = new_password
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        new_password_send_to_email.delay(instance.email, new_password)
        return Response(serializer.data, status=status.HTTP_200_OK)