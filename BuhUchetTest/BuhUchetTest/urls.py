from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.Accounts.urls', namespace='accounts')),
    path('api/', include('apps.ToDo.urls', namespace='todo')),
]
