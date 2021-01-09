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
    
    def get_user(self):
        return self.User.objects.create_superuser(self.email, self.password)

    def login_user(self):
        user = self.User.objects.create(email=self.email, password=self.password)
        self.client.force_login(user)
    
    def login_admin(self):
        user = self.User.objects.create(email=self.email, password=self.password)
        user.is_admin = True
        user.save()
        self.client.force_login(user)


@skip
class ViewTest(BaseTestCase):

    def test_library_returns_page_status_ok(self):
        url_name = 'app:url_name'
        response = Client().get(reverse(url_name))
        self.assertEqual(response.status_code, 200)