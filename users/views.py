from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from users import forms, models

from users.services import send_user_activation_link

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

class UsersAccountActivationView(TemplateView):
    pass