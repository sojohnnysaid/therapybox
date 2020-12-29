from django.test import TestCase, Client
from django.contrib.auth import get_user_model


class UsersBaseTestCase(TestCase):

    def create_test_user(self, name):
        email = f'{name}@gmail.com'
        password = 'pP@assW0rd'
        return get_user_model().objects.create_user(email=email, password=password)