from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from ..models import ToDo

User = get_user_model()
client = APIClient()


class ToDoTests(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='casper', email='casper@mail.ru', password='password123')
        self.todo1 = ToDo.objects.create(headline='headline1', description='description1')
        self.todo2 = ToDo.objects.create(headline='headline2', description='description2')
        return super().setUp()


    def test_todo_list(self):
        '''Проверить получение списка задач
        '''
        url = reverse('todo:todolist_create')
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ToDo.objects.count(), len(response.data))


    def test_todo_create(self):
        '''Проверить создание задачи и игнорирование поля execute, должна быть execute=False
        '''
        url = reverse('todo:todolist_create')
        body = {
            "headline":"New headline",
            "description":"New description",
            "deadline":"2022-10-30 15:37",
            "execute":"True"
        }
        response = client.post(url, body, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ToDo.objects.count(), 3)
        self.assertEqual(ToDo.objects.get(headline='New headline').execute, False)


    def test_todo_get(self):
        '''Проверить получение одной задачи
        '''
        url = reverse('todo:todogetupdel', kwargs={'pk':1})
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.token)
        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('id'), 1)


    def test_todo_update(self):
        '''Проверить редактирование задачи.
        '''
        url = reverse('todo:todogetupdel', kwargs={'pk':1})
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.token)
        body = {
            "headline":"Change headline",
            "description":"Change description",
        }
        response = client.patch(url, body, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ToDo.objects.get(headline='Change headline').description, 'Change description')


    def test_todo_update_deadline(self):
        '''Проверить валидацию поля deadline.
        '''
        url = reverse('todo:todogetupdel', kwargs={'pk':1})
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.token)
        body = {
                'deadline': '2012-10-31 15:20+00:00'
        }
        response = client.patch(url, body, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_todo_delete(self):
        '''Проверить удаление задачи.
        '''
        url = reverse('todo:todogetupdel', kwargs={'pk':1})
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.token)
        response = client.delete(url, None, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ToDo.objects.count(), 1)


    def test_todo_execute_change(self):
        '''Проверить отметить задачу выполненной .
        '''
        url = reverse('todo:todoexecute', kwargs={'pk':1})
        client.credentials(HTTP_AUTHORIZATION='Token ' + self.user.token)
        response = client.patch(url, None, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ToDo.objects.get(id='1').execute, True)