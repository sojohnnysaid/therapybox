from django.contrib import admin
from django.urls import path
from django.views.debug import default_urlconf

urlpatterns = [
    path('debug/', default_urlconf, name='debug'),
    path('admin/', admin.site.urls),
]
