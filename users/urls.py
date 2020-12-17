# users urls
from django.urls import path
from users.views import UsersRegisterView

urlpatterns = [
    path('register/', UsersRegisterView.as_view(), name='users_register'),
]
