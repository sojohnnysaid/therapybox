from unittest import skip
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from factories.factories import TherapyBoxUserFactory




class BaseTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.user = TherapyBoxUserFactory()
        self.client = Client()
        



class UserCanRegisterViewTest(BaseTestCase):

    def test_library_view_returns_page_status_ok(self):
        self.client.login(email=self.user.email, password='password')
        response = self.client.get(reverse('therapybox:list_library'))
        self.assertEqual(response.status_code, 200)

    def test_register_view_returns_page_status_ok(self):
        response = Client().get(reverse('users:register'))
        self.assertEqual(response.status_code, 200)