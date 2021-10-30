from django.urls import path

from .views import ToDoListApiView, ToDoGetUpdateDelApiView, ToDoExecuteApiView

app_name = 'todo'

urlpatterns = [
    path('todo/', ToDoListApiView.as_view(), name='todolist_create'),
    path('todo/<int:pk>/', ToDoGetUpdateDelApiView.as_view(), name='todogetupdel'),
    path('todo/<int:pk>/execute/', ToDoExecuteApiView.as_view(), name='todoexecute'),
]