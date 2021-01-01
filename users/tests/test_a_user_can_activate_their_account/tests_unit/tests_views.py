import re
from urllib.parse import urlparse
from django.urls import reverse, reverse_lazy
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils import timezone
from django.core import mail
from django.test import TestCase, Client
from django.conf import settings as conf_settings

from unittest.case import skip
from unittest.mock import patch

from users import views, models, forms, services
from users.tokens import default_account_activation_token_generator as token_generator




class BaseTestCase(TestCase):

    def setUp(self):
        super().setUp()
        data = {
            'email': 'johasdfasdfsdn@gmail.com',
            'first_name': 'johasdfdsn',
            'password1': 'p@assW0rd',
            'password2': 'p@assW0rd'}

        response = Client().post(reverse_lazy('users:register'), data, follow=True)
        
        email = mail.outbox[0]
        url_search = re.search(r'http://.+/users/account-activation/\?uid=.+&token=.+$', email.body)
        self.link = url_search.group(0)




class UsersAccountActivationViewTest(BaseTestCase):

    # use Client instead of RequestFactory in tests because messages will not work otherwise
    @patch('users.views.services')
    def test_calls_activate_user_service(self, mock_services):
        Client().get(self.link)
        mock_services.activate_user.assert_called_once()

    @patch('users.views.services')
    def test_correct_arguments_passed_to_activate_user_service(self, mock_services):
        response = Client().get(self.link)
        initial_request = response.wsgi_request
        mock_services.activate_user.assert_called_once_with(initial_request)

    def test_redirect(self):
        response = Client().get(self.link)
        self.assertRedirects(response, reverse('users:login'))