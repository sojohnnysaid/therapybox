from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth import get_user_model, logout, login
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.http.response import HttpResponse
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages

from users.tokens import default_account_activation_token_generator as token_generator
from . import forms, models


# Create your views here.
class UsersRegisterView(CreateView):
    model = models.CustomUser
    form_class = forms.UsersRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:users_register_form_submitted')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        user = self.object
        
        link = self.request.build_absolute_uri(reverse_lazy('users:users_account_activation'))
        url_safe_user_pk = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)

        send_mail(
            'Here is your activation link',
            f'{link}?uid={url_safe_user_pk}&token={token}',
            'from@example.com',
            [user.email],
            fail_silently=False,
        )
        return super().form_valid(form)


class UsersRegisterFormSubmittedView(TemplateView):
    template_name = 'users/register_form_submitted.html'


class UsersAccountActivationView(TemplateView):
    success_message = 'Your account has been activated! You can now login'

    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        user_pk = urlsafe_base64_decode(request.GET.get('uid')).decode('utf-8')
        user = get_user_model().objects.get(pk=user_pk)

        if not token_generator.check_token(user, token):
            return HttpResponse("sorry this token has already been used! <a href='#'>Back to homepage</a>")

        user.is_active = True
        user.save()

        messages.success(request, 'Your account has been activated! You can now login')
        return redirect(reverse_lazy('users:users_login'))


class UsersLoginView(TemplateView):
    template_name = 'users/login.html'