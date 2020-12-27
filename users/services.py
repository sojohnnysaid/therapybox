from django.core.mail import send_mail
from django.urls.base import reverse_lazy
from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from users.tokens import default_account_activation_token_generator as token_generator


def send_account_activation_link(request, user):
    def get_activation_link(request, user):
        token = token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        absolute_uri = request.build_absolute_uri(reverse_lazy('users:account_activation'))
        return f'{absolute_uri}?uid={uid}&token={token}'

    email_subject = 'Here is your activation link'
    email_body = get_activation_link(request,user)
    email_from = 'noreply@example.com'
    email_to = [user.email]

    return send_mail(
        email_subject,
        email_body,
        email_from,
        email_to,
        fail_silently=False,
    )