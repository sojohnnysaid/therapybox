# users urls
from django.urls import path
from users.views import (
    UsersRegisterView, 
    UsersRegisterFormSubmittedView,
    UsersAccountActivationView,
    UsersLoginView,
    UsersForgotPasswordResetRequestView,
    UsersForgotPasswordResetView)

app_name = 'users'
urlpatterns = [
    path('register/', UsersRegisterView.as_view(), name='register'),
    path('register-form-submitted/', UsersRegisterFormSubmittedView.as_view(), name='register_form_submitted'),
    path('account-activation/', UsersAccountActivationView.as_view(), name='account_activation'),
    path('login/', UsersLoginView.as_view(), name='login'),
    path('password-request-reset-link/', UsersForgotPasswordResetRequestView.as_view(), name='password_request_reset_link'),
    path('password-reset/<uidb64>/<token>/', UsersForgotPasswordResetView.as_view(), name='password-reset'),
]