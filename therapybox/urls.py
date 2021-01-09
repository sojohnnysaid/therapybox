# users urls
from django.urls import path
from django.views.generic import TemplateView
from therapybox.views import *

app_name = 'therapybox'
urlpatterns = [
    path('', LibraryList.as_view(), name='list_library'),
    path('<int:pk>', LibraryDetail.as_view(), name='detail_library'),
]