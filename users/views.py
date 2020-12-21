from django.core.mail import send_mail
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from . import forms, models


# Create your views here.
class UsersRegisterView(CreateView):
    model = models.TestModel
    form_class = forms.UsersRegisterForm
    template_name = 'users/users_register.html'
    success_url = reverse_lazy('users:users_register_form_submitted')

    def post(self, request, *args, **kwargs):
        user_email_address = request.POST['email']
        link = request.build_absolute_uri(reverse_lazy('users:users_account'))
        send_mail(
            'Here is your activation link',
            f'{link}?token=blahblahblah',
            'from@example.com',
            [user_email_address],
            fail_silently=False,
        )
        return super().post(request, *args, **kwargs)


class UsersRegisterFormSubmittedView(TemplateView):
    template_name = 'users/users_register_form_submitted.html'


class UsersAccountView(TemplateView):
    template_name = 'users/users_account.html'
