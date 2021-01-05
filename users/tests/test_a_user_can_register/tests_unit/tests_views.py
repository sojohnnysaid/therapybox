from unittest import skip
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model




class BaseTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.User = get_user_model()



class UserCanRegisterViewTest(BaseTestCase):

    def test_homepage_view_returns_page_status_ok(self):
        response = Client().get(reverse('therapybox:homepage'))
        self.assertEqual(response.status_code, 200)

    def test_register_view_returns_page_status_ok(self):
        response = Client().get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)