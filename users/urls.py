# users urls
from django.urls import path
from users.views import *

app_name = 'users'
urlpatterns = [
    path('register/', UsersRegisterView.as_view(), name='register'),
    path('profile/<int:pk>', UsersProfileView.as_view(), name='profile'),
    path('account-activation/', UsersAccountActivationView.as_view(), name='account_activation'),
    path('account-activation-request/', UsersAccountActivationRequestView.as_view(), name='account_activation_request'),
    path('password-request-reset-link/', UsersPasswordResetRequestView.as_view(), name='password_request_reset_link'),
    path('password-reset/<uidb64>/<token>/', UsersPasswordResetView.as_view(), name='password_reset'),
    path('login/', UsersLoginView.as_view(), name='login'),
    path('logout/', UsersLogoutView.as_view(next_page='/'), name='logout'),
    path('admin-login/', UsersAdminLoginView.as_view(), name='admin_login'),
]