from django.http import HttpResponseRedirect
from django.urls.base import reverse
from django.views.generic.base import RedirectView, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib import messages

from users import forms, models

from users.services import send_user_activation_link, activate_user

# Create your views here.
class UsersRegisterView(CreateView):
    model = models.CustomUser
    form_class = forms.UsersRegisterForm
    template_name = 'users/users_register.html'
    success_url = reverse_lazy('users:register_form_submitted')

    def form_valid(self, form):
        self.object = form.save()
        send_user_activation_link(self.request, self.object)
        return HttpResponseRedirect(self.get_success_url())

class UsersRegisterFormSubmittedView(TemplateView):
    template_name = 'users/users_register_form_submitted.html'

class UsersAccountActivationView(RedirectView):
    url = reverse_lazy('users:login')
    def get(self, request, *args, **kwargs):
        activate_user(request)
        return super().get(request, *args, **kwargs)

class UsersLoginView(TemplateView):
    template_name = 'users/users_login.html'