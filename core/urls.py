from django.contrib import admin
from django.urls import path, include
from django.views.debug import default_urlconf

urlpatterns = [
    path('', include('therapybox.urls')),
    path('debug/', default_urlconf, name='debug'),
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
]
