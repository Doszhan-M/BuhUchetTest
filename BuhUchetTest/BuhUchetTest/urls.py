from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .yasg import urlpatterns as yasg_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.Accounts.urls', namespace='accounts')),
    path('api/', include('apps.ToDo.urls', namespace='todo')),
]

urlpatterns += yasg_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)