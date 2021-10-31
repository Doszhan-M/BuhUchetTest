from django.test import TestCase

from ..models import User
from ..serializers import RegistrationSerializer, LoginSerializer, UserSerializer


class AccountSerializersTestCase(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='casper', email='casper@mail.ru', password='password123')
        return super().setUp()


    def test_RegistrationSerializer(self):
        '''Проверить сериализацию RegistrationSerializer
        '''
        serializer_data = RegistrationSerializer(self.user).data
        expected_data = {
                'email': 'casper@mail.ru',
                'username': 'casper',
                'token': self.user.token
            }
        self.assertEqual(serializer_data, expected_data)


    def test_LoginSerializer(self):
        '''Проверить сериализацию LoginSerializer
        '''
        serializer_data = LoginSerializer(self.user).data
        expected_data = {
                'email': 'casper@mail.ru',
                'username': 'casper',
                'token': self.user.token
            }
        self.assertEqual(serializer_data, expected_data)


    def test_UserSerializer(self):
        '''Проверить сериализацию UserSerializer
        '''
        serializer_data = UserSerializer(self.user).data
        expected_data = {
                'email': 'casper@mail.ru',
                'username': 'casper',
                'token': self.user.token
            }
        self.assertEqual(serializer_data, expected_data)