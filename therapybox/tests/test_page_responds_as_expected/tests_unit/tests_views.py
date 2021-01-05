from unittest import skip
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model




class BaseTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.User = get_user_model()
        self.email = 'test@gmail.com'
        self.password = 'password'
        self.client = Client()

    def login_user(self):
        user = self.User.objects.create(email=self.email, password=self.password)
        self.client.force_login(user)
    
    def login_admin(self):
        user = self.User.objects.create(email=self.email, password=self.password)
        user.is_admin = True
        user.save()
        self.client.force_login(user)


class ViewTest(BaseTestCase):

    # public routes

    def test_homepage_returns_page_status_ok(self):
        url_name = 'debug'
        response = self.client.get(reverse(url_name))
        self.assertEqual(response.status_code, 200)

    def test_register_returns_page_status_ok(self):
        url_name = 'users:register'
        response = self.client.get(reverse(url_name))
        self.assertEqual(response.status_code, 200)

    def test_account_activation_request_returns_page_status_ok(self):
        url_name = 'users:account_activation_request'
        response = self.client.get(reverse(url_name))
        self.assertEqual(response.status_code, 200)

    def test_password_request_reset_link_returns_page_status_ok(self):
        url_name = 'users:password_request_reset_link'
        response = self.client.get(reverse(url_name))
        self.assertEqual(response.status_code, 200)

    def test_user_login_returns_page_status_ok(self):
        url_name = 'users:login'
        response = self.client.get(reverse(url_name))
        self.assertEqual(response.status_code, 200)
    
    