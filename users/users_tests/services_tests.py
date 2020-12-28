from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from unittest.mock import patch

from users import services

class GetActivationLinkTest(TestCase):

    def test_get_activation_link_returns_expected_url(self):
        email = 'johnsmith@gmail.com'
        response = Client().post(reverse('users:register_form'), {
            'email': email,
            'first_name': 'John',
            'password1': 'p@assW0rd',
            'password2': 'p@assW0rd'
        })
        initial_request = response.wsgi_request
        user = get_user_model().objects.get(email=email)
        activation_link = services.get_activation_link(initial_request, user)
        self.assertRegex(activation_link, r'http://.+/users/account-activation/\?uid=.+&token=.+$')




class SendUserActivationTest(TestCase):

    @patch('users.services.get_activation_link')
    def test_get_activation_link_called(self, mock_get_activation_link):
        Client().post(reverse('users:register_form'), {
            'email': 'johnsmith@gmail.com',
            'first_name': 'John',
            'password1': 'p@assW0rd',
            'password2': 'p@assW0rd'
        })
        mock_get_activation_link.assert_called_once()

    @patch('users.services.send_mail')
    def test_calls_send_mail(self, mock_send_mail):
        email = 'johnsmith@gmail.com'
        response = Client().post(reverse('users:register_form'), {
            'email': email,
            'first_name': 'John',
            'password1': 'p@assW0rd',
            'password2': 'p@assW0rd'
        })
        initial_request = response.wsgi_request
        user = get_user_model().objects.get(email=email)
        activation_link = services.get_activation_link(initial_request, user)
        Client().get(activation_link)
        mock_send_mail.assert_called_once()




class ActivateUserTest(TestCase):

    @patch('users.services.messages')
    def test_calls_success_message(self, mock_messages):
        email = 'johnsmith@gmail.com'
        response = Client().post(reverse('users:register_form'), {
            'email': email,
            'first_name': 'John',
            'password1': 'p@assW0rd',
            'password2': 'p@assW0rd'
        })
        initial_request = response.wsgi_request
        user = get_user_model().objects.get(email=email)
        activation_link = services.get_activation_link(initial_request, user)
        Client().get(activation_link)
        mock_messages.success.assert_called_once()

    @patch('users.services.messages')
    def test_calls_error_message(self, mock_messages):
        email = 'johnsmith@gmail.com'
        response = Client().post(reverse('users:register_form'), {
            'email': email,
            'first_name': 'John',
            'password1': 'p@assW0rd',
            'password2': 'p@assW0rd'
        })
        initial_request = response.wsgi_request
        user = get_user_model().objects.get(email=email)
        activation_link = services.get_activation_link(initial_request, user)
        Client().get(activation_link)
        # request page again to invalidate token
        Client().get(activation_link)
        mock_messages.error.assert_called_once()