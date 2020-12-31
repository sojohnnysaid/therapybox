from django.contrib.auth.views import PasswordResetConfirmView
from django.http import HttpResponseRedirect
from django.urls.base import reverse
from django.views.generic.base import RedirectView, TemplateView
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import get_user_model

from users import forms, models, services

from django.conf import settings as conf_settings


# Create your views here.
class UsersRegisterView(CreateView):
    model = models.CustomUser
    form_class = forms.UsersRegisterForm
    template_name = 'users/register.html'
    success_url = conf_settings.USERS_REGISTER_SUCCESS_URL

    def form_valid(self, form):
        self.object = form.save()
        services.send_user_activation_link(self.request, self.object)
        return HttpResponseRedirect(self.get_success_url())




class UsersRegisterFormSubmittedView(TemplateView):
    template_name = 'users/register_form_submitted.html'




class UsersAccountActivationView(RedirectView):
    url = reverse_lazy('users:login')
    def get(self, request, *args, **kwargs):
        services.activate_user(request)
        return super().get(request, *args, **kwargs)




class UsersLoginView(TemplateView):
    template_name = 'users/login.html'




class UsersForgotPasswordResetRequestView(FormView):
    template_name = 'users/password_reset_request.html'
    form_class = forms.UsersPasswordResetRequestForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = get_user_model().objects.get(email=form.cleaned_data['email'])
        services.send_password_reset_link(self.request, user)
        return HttpResponseRedirect(self.success_url)




INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'
class UsersForgotPasswordResetView(PasswordResetConfirmView):
    success_url = reverse_lazy('users:login')
    template_name = 'users/password_reset_form.html'

    def form_valid(self, form):
        del self.request.session[INTERNAL_RESET_SESSION_TOKEN]
        messages.success(self.request, 'Success! Your password has been reset.')
        return HttpResponseRedirect(self.success_url)