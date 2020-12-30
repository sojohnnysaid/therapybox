from urllib.parse import urlparse

from unittest.case import skip
from django.test import TestCase
from django.test.client import Client, RequestFactory
from django.urls import resolve, reverse

from users import services, views
from users.tests_users import base

'''
Does the reverse method resolve to the correct path?
Does the ResolverMatch class call the correct view?

resolve gives us back the ResolverMatch class
it has the path in it's route attribute
it has the class in the func.view_class attribute

code to implement:
to make these tests pass you will have to create
the url pattern and declare the class in views
'''



class RegisterURLTest(TestCase):

    def test_resolves_to_correct_path(self):
        expected_path = 'users/register/'
        name = 'users:register'
        resolver_match = resolve(reverse(name))
        resolved_path = resolver_match.route
        self.assertEqual(expected_path, resolved_path)

    def test_calls_correct_view(self):
        expected_class = views.UsersRegisterView
        name = 'users:register'
        resolver_match = resolve(reverse(name))
        resolved_class = resolver_match.func.view_class
        self.assertEqual(expected_class, resolved_class)




class RegisterFormSubmittedURLTest(TestCase):

    def test_resolves_to_correct_path(self):
        expected_path = 'users/register-form-submitted/'
        name = 'users:register_form_submitted'
        resolver_match = resolve(reverse(name))
        resolved_path = resolver_match.route
        self.assertEqual(expected_path, resolved_path)

    def test_calls_correct_view(self):
        expected_class = views.UsersRegisterFormSubmittedView
        name = 'users:register_form_submitted'
        resolver_match = resolve(reverse(name))
        resolved_class = resolver_match.func.view_class
        self.assertEqual(expected_class, resolved_class)




class AccountActivationURLTest(TestCase):

    def test_resolves_to_correct_path(self):
        expected_path = 'users/account-activation/'
        name = 'users:account_activation'
        resolver_match = resolve(reverse(name))
        resolved_path = resolver_match.route
        self.assertEqual(expected_path, resolved_path)

    def test_calls_correct_view(self):
        expected_class = views.UsersAccountActivationView
        name = 'users:account_activation'
        resolver_match = resolve(reverse(name))
        resolved_class = resolver_match.func.view_class
        self.assertEqual(expected_class, resolved_class)




class LoginURLTest(TestCase):

    def test_resolves_to_correct_path(self):
        expected_path = 'users/login/'
        name = 'users:login'
        resolver_match = resolve(reverse(name))
        resolved_path = resolver_match.route
        self.assertEqual(expected_path, resolved_path)

    def test_calls_correct_view(self):
        expected_class = views.UsersLoginView
        name = 'users:login'
        resolver_match = resolve(reverse(name))
        resolved_class = resolver_match.func.view_class
        self.assertEqual(expected_class, resolved_class)




class ForgotPasswordResetRequestURLTest(TestCase):
    
    def test_resolves_to_correct_path(self):
        expected_path = 'users/forgot-password-reset-request/'
        name = 'users:forgot_password_reset_request'
        resolver_match = resolve(reverse(name))
        resolved_path = resolver_match.route
        self.assertEqual(expected_path, resolved_path)
        
    def test_resolves_to_correct_view(self):
        expected_class = views.UsersForgotPasswordResetRequestView
        name = 'users:forgot_password_reset_request'
        resolver_match = resolve(reverse(name))
        resolved_class = resolver_match.func.view_class
        self.assertEqual(expected_class, resolved_class)




class ForgotPasswordResetURLTest(base.UsersBaseTestCase):
    
    def test_resolves_to_correct_path(self):
        user = self.create_test_user('John')
        request = RequestFactory().get('') # request path not important in this case
        url = services.get_password_reset_link(request, user)
        response = Client().get(url)
        expected_path = 'users/forgot-password-reset/'
        self.assertTrue(expected_path in response.url)

    def test_resolves_to_correct_view(self):
        user = self.create_test_user('John')
        request = RequestFactory().get('') # request path not important in this case
        url = services.get_password_reset_link(request, user)
        path = urlparse(url).path
        
        expected_class = views.UsersForgotPasswordResetView
        resolver_match = resolve(path)
        resolved_class = resolver_match.func.view_class
        self.assertEqual(expected_class, resolved_class)