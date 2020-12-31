# users urls
from django.urls import path
from django.views.generic import TemplateView

app_name = 'therapybox'
urlpatterns = [
    path('', TemplateView.as_view(template_name='therapybox/homepage.html'), name='homepage'),
]