from unittest import skip
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls.base import reverse




class BaseTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.email = 'john@gmail.com'
        self.password = 'pP@assW0rd'
        self.user = get_user_model().objects.create_user(email=self.email, password=self.password)
        self.user.is_active = False
        self.user.save()




class LoginRaisesValidationErrorWhenAccountNotActiveTest(BaseTestCase):

    def test_login_form_raises_validation_error_when_user_is_not_active(self):
        pass