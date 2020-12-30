# users urls
from django.urls import path
from users.views import (
    UsersRegisterView, 
    UsersRegisterFormSubmittedView,
    UsersAccountActivationView,
    UsersLoginView,
    UsersPasswordResetRequestView,
    UsersPasswordResetView)

app_name = 'users'
urlpatterns = [
    path('register/', UsersRegisterView.as_view(), name='register'),
    path('register-form-submitted/', UsersRegisterFormSubmittedView.as_view(), name='register_form_submitted'),
    path('account-activation/', UsersAccountActivationView.as_view(), name='account_activation'),
    path('login/', UsersLoginView.as_view(), name='login'),
    path('forgot-password-reset-request/', UsersPasswordResetRequestView.as_view(), name='forgot_password_reset_request'),
    path('forgot-password-reset-form/<uidb64>/<token>/', UsersPasswordResetView.as_view(), name='forgot_password_reset_form'),
]