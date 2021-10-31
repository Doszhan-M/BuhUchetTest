from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


User = get_user_model()
client = APIClient()


class AccountTests(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='casper', email='casper@mail.ru', password='password123')
        return super().setUp()

    def test_register_account(self):
        '''Проверить регистрацию пользователя
        '''
        url = reverse('accounts:signup')
        body = {
            "user": {
                "username": 'username1',
                "email": 'casper@mail.ru1',
                "password": 'password123'
            }
        }
        response = client.post(url, body, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(
            email='casper@mail.ru1').username, 'username1')

    def test_login_account(self):
        '''Проверить авторизацию пользователя
        '''
        url = reverse('accounts:login')
        body = {
            "user": {
                "email": self.user.email,
                "password": 'password123'
            }
        }
        response = client.post(url, body, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data.get('token')), 0)

    def test_get_user(self):
        '''Проверить получения пользователя
        '''
        url = reverse('accounts:user')
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.token)
        response = client.get(url, None, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('username'), 'casper')

    def test_update_user(self):
        '''Проверить обновление данных пользователя.
        '''
        url = reverse('accounts:user')
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.token)
        body = {
            "user": {
                'username': 'newcasper'
            }
        }
        response = client.patch(url, body, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.first().username, 'newcasper')

    def test_pass_reset(self):
        '''Проверить сброс пароля пользователя.
        '''
        preview_pass = self.user.password
        url = reverse('accounts:pass_reset')
        body = {
            "user": {
                'email': self.user.email
            }
        }
        response = client.patch(url, body, format='json')
        self.user.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        new_pass = self.user.password
        self.assertNotEqual(preview_pass, new_pass)
