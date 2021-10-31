from django.test import TestCase

from ..models import ToDo
from ..serializers import ToDoListserializer, ToDoserializer


class ToDoSerializersTestCase(TestCase):
    
    def setUp(self) -> None:
        self.todo1 = ToDo.objects.create(headline='headline1', description='description1', deadline='2022-10-31 15:20+00:00')
        self.todo2 = ToDo.objects.create(headline='headline2', description='description2', execute=True)
        return super().setUp()


    def test_ToDoListserializer(self):
        '''Проверить сериализацию ToDoListserializer
        '''
        serializer_data = ToDoListserializer([self.todo1, self.todo2], many=True).data
        expected_data = [
            {
                'id': self.todo1.id,
                'headline': 'headline1',
                'description': 'description1',
                'deadline': '2022-10-31 15:20+00:00',
                'execute': False
            },
            {
                'id': self.todo2.id,
                'headline': 'headline2',
                'description': 'description2',
                'deadline': None,
                'execute': True
            },
        ]
        self.assertEqual(serializer_data, expected_data)


    def test_ToDoserializer(self):
        '''Проверить сериализацию ToDoserializer
        '''
        serializer_data = ToDoserializer(self.todo1).data
        expected_data = {
                'id': self.todo1.id,
                'headline': 'headline1',
                'description': 'description1',
                'deadline': '2022-10-31 15:20+00:00',
                'execute': False
            }
        self.assertEqual(serializer_data, expected_data)