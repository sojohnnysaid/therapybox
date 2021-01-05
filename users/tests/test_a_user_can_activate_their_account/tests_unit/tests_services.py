from django.test import TestCase, Client, RequestFactory
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.core import mail

from unittest.mock import patch

from users import services





class BaseTestCase(TestCase):

    def setUp(self):
        super().setUp()

        data = {
            'email': 'john@gmail.com',
            'password1': 'p@assW0rd',
            'password2': 'p@assW0rd',
            'facility_name': 'foo',
            'company_name': 'foo',
            'phone_number': 'foo',
            'point_of_contact': 'foo',
            'address_line_1': 'foo',
            'address_line_2': 'foo',
            'suburb': 'foo',
            'city': 'foo',
            'postcode': 'foo',
            'shipping_region': 'REGION_1',
            'agreed_to_terms_and_conditions': 'True',
            }

        self.response = Client().post(reverse_lazy('users:register'), data)



class ActivateUserTest(BaseTestCase):

    @patch('users.services.messages')
    def test_account_activation_link_only_works_once(self, mock_messages):
        initial_request = self.response.wsgi_request
        user = get_user_model().objects.get(email='john@gmail.com')
        activation_link = services.get_activation_link(initial_request, user)
        
        Client().get(activation_link)
        # request page again to invalidate token
        Client().get(activation_link)

        mock_messages.error.assert_called_once()
        
    @patch('users.services.messages')
    def test_account_activation_service_calls_success_message(self, mock_messages):
        initial_request = self.response.wsgi_request
        user = get_user_model().objects.get(email='john@gmail.com')
        activation_link = services.get_activation_link(initial_request, user)
        
        Client().get(activation_link)

        mock_messages.success.assert_called_once()

