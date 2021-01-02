# users urls
from django.urls import path
from django.contrib.auth.views import LogoutView
from users.views import (
    UsersRegisterView, 
    UsersAccountActivationView,
    UsersLoginView,
    UsersPasswordResetRequestView,
    UsersPasswordResetView)

app_name = 'users'
urlpatterns = [
    path('register/', UsersRegisterView.as_view(), name='register'),
    path('account-activation/', UsersAccountActivationView.as_view(), name='account_activation'),
    path('password-request-reset-link/', UsersPasswordResetRequestView.as_view(), name='password_request_reset_link'),
    path('password-reset/<uidb64>/<token>/', UsersPasswordResetView.as_view(), name='password-reset'),
    path('login/', UsersLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout')
]