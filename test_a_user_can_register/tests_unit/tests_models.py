from django.test import TestCase, Client
from django.contrib.auth import get_user_model



class BaseTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.User = get_user_model()



class UserCanRegisterModelTest(BaseTestCase):

    def test_user_model_creation(self):
        user_object = self.User.objects.create(
            email='test@gmail.com',
            password='password',
            facility_name='foo facility',
            company_name='foo company',
            phone_number='123-123-1234',
            point_of_contact='John Smith',
            address_line_1='111 foo street',
            address_line_2='door 1 foo',
            suburb='foo subrub',
            city='foo city',
            postcode='12391',
            shipping_region='REGION_1',
            agreed_to_terms_and_conditions=True,
            is_approved=False,
        )
        self.assertIsInstance(user_object, get_user_model())
