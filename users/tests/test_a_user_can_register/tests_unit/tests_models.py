from django.test import TestCase, Client
from django.contrib.auth import get_user_model



class BaseTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.User = get_user_model()



class UserCanRegisterModelTest(BaseTestCase):

    def test_user_model_creation(self):
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
            'password': 'p@assW0rd',
        }
        user_object = self.User.objects.create(**data)
        self.assertIsInstance(user_object, get_user_model())
