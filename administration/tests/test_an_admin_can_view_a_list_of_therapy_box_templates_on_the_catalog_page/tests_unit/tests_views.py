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
        self.User.objects.create_superuser(self.email, self.password)

    def login(self, name):
       return Client().post(
            reverse(name), 
            {'username': self.email, 'password': self.password}, follw=True)


@skip
class ViewTest(BaseTestCase):

    def test_homepage_returns_page_status_ok(self):
        url_name = 'app:url_name'
        response = Client().get(reverse(url_name))
        self.assertEqual(response.status_code, 200)