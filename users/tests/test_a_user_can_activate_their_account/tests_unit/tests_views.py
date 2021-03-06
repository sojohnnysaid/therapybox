import re
from django.urls import reverse, reverse_lazy
from django.core import mail
from django.test import TestCase, Client
from django.conf import settings as conf_settings
from unittest.mock import patch





class BaseTestCase(TestCase):

    def setUp(self):
        super().setUp()
        data = {
            'email': 'john@gmail.com',
            'facility_name': 'foo',
            'company_name': 'foo',
            'phone_number': 'foo',
            'point_of_contact': 'foo',
            'billing_address_line_1': 'foo',
            'billing_address_line_2': 'foo',
            'billing_suburb': 'foo',
            'billing_city': 'foo',
            'billing_postcode': 'foo',
            'shipping_address_line_1': 'foo',
            'shipping_address_line_2': 'foo',
            'shipping_suburb': 'foo',
            'shipping_city': 'foo',
            'shipping_postcode': 'foo',
            'shipping_region': 'REGION_1',
            'agreed_to_terms_and_conditions': 'True',
            'password1': 'p@assW0rd',
            'password2': 'p@assW0rd',
        }

        response = Client().post(reverse_lazy('users:register'), data, follow=True)
        
        email = mail.outbox[0]
        url_search = re.search(r'http://.+/account-activation/\?uid=.+&token=.+$', email.body)
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
        self.assertRedirects(response, conf_settings.LOGOUT_URL)