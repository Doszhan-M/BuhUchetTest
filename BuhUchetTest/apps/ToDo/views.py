from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import ToDoListserializer, ToDoserializer
from .models import ToDo


class ToDoListApiView(generics.ListCreateAPIView):
    '''Получение списка задач, создать задачу.
    '''
    queryset = ToDo.objects.all()
    serializer_class = ToDoListserializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        response = super(ToDoListApiView, self).get(request, *args, **kwargs)
        for obj in response.data:
            obj.pop('description')
        return response

    
class ToDoGetUpdateDelApiView(generics.RetrieveUpdateDestroyAPIView):
    '''Получить, обновить или удалить задачу.
    '''
    queryset = ToDo.objects.all()
    serializer_class = ToDoserializer
    permission_classes = (IsAuthenticated,)


class ToDoExecuteApiView(generics.UpdateAPIView):
    '''Пометить задачу выполненной.
    '''
    queryset = ToDo.objects.all()
    serializer_class = ToDoserializer
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data
        serializer_data['execute'] = True
        instance = self.get_object()
        serializer = self.serializer_class(
            instance, data=serializer_data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
