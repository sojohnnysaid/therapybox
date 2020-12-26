from django.core.mail import send_mail
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from users import forms, models

from users.services.account_activation import send_activation_link

# Create your views here.
class UsersRegisterView(CreateView):
    model = models.CustomUser
    form_class = forms.UsersRegisterForm
    template_name = 'users/users_register.html'
    success_url = reverse_lazy('users:users_register_form_submitted')

    def form_valid(self, form):
        """If the form is valid, save self.object, which is the user."""
        self.object = form.save()
        send_activation_link(self.request, self.object)
        return super().form_valid(form)


class UsersRegisterFormSubmittedView(TemplateView):
    template_name = 'users/users_register_form_submitted.html'


class UsersAccountView(TemplateView):
    template_name = 'users/users_account.html'
