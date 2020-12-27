from django.core.mail import send_mail
from django.urls.base import reverse_lazy
from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from users.tokens import default_account_activation_token_generator as token_generator


def get_account_activation_email_subject():
    return 'Here is your activation link'

def test_get_account_activation_email_message(request):
    user = get_user_model().objects.get(email=request.POST['email'])
    token = token_generator.make_token(user)
    url_safe_user_pk = urlsafe_base64_encode(force_bytes(user.pk))
    link = request.build_absolute_uri(reverse_lazy('users:users_account_activation'))
    message = f'{link}?uid={url_safe_user_pk}&token={token}'
    return message

def get_account_activation_from_email():
    return 'noreply@example.com'

def get_account_activation_user_email(request):
    return request.POST['email']

def send_activation_link(request):
    return send_mail(
        get_account_activation_email_subject(),
        test_get_account_activation_email_message(request),
        get_account_activation_from_email(),
        [get_account_activation_user_email(request)],
        fail_silently=False,
    )