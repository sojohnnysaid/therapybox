# users urls
from django.urls import path
from users.views import (
    UsersRegisterView, 
    UsersRegisterFormSubmittedView,
    UsersAccountActivationView,
    UsersLoginView)

app_name = 'users'
urlpatterns = [
    path('register/', UsersRegisterView.as_view(), name='register_form'),
    path('register-form-submitted/', UsersRegisterFormSubmittedView.as_view(), name='register_form_submitted'),
    path('account-activation/', UsersAccountActivationView.as_view(), name='account_activation'),
    path('login/', UsersLoginView.as_view(), name='login'),
]
