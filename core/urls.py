from django.contrib import admin
from django.urls import path, include
from django.views.debug import default_urlconf

urlpatterns = [
    path('', include('users.urls')),
    path('', include('therapybox.urls')),
    path('admin/', include('administration.urls')),
    path('debug/', default_urlconf, name='debug'),
    path('control-panel/', admin.site.urls),
]
