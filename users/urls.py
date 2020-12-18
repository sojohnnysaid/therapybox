# users urls
from django.urls import path
from users.views import UsersRegisterView, UsersRegisterFormSubmittedView

urlpatterns = [
    path('register/', UsersRegisterView.as_view(), name='users_register'),
    path('register-form-submitted/', UsersRegisterFormSubmittedView.as_view(), name='users_register_form_submitted'),
]
