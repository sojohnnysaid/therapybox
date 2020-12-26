'''
How this class works
1. An HTTP request comes in for a particular URL
2. Django uses some rules to decide which view function should deal with the request (this is referred to as respolving the URL)
3. The view function processes the request and returns and HTTP response
'''

'''
We test:
1. Can we resolve the requested URL to a particular view function we've made?
2. Can we make this view function return HTML which will get the functional test to pass?
3. Can we access the correct model when we create a view instance?
'''

from unittest.case import skip
from django.urls import reverse
from django.core import mail
from django.test import TestCase
from django.test import RequestFactory

from unittest.mock import patch, Mock
import pytest

from users import views, models, forms

class UsersRegisterViewTest(TestCase):

    def setUp(self):
        self.request = RequestFactory().post(reverse('users:users_register'), {
            'email': 'johnsmith@gmail.com', 
            'first_name': 'John', 
            'password1': 'p@assW0rd', 
            'password2': 'p@assW0rd'})

    def test_uses_CustomUser(self):
        assert views.UsersRegisterView.model == models.CustomUser
        
    def test_uses_UsersRegisterForm(self):
        assert views.UsersRegisterView.form_class == forms.UsersRegisterForm

    def test_uses_expected_template(self):
        assert views.UsersRegisterView.template_name == 'users/users_register.html'

    @patch('users.views.send_mail', autospec=True)
    def test_email_sent_on_POST_request(self, mock_send_mail):
        views.UsersRegisterView.as_view()(self.request)
        print('\nmock_send_email:', mock_send_mail.call_args)
        # email = mail.outbox[0]
        # assert 'Here is your activation link' in email.subject

    # def test_redirects_on_POST_request(self):
    #     response = self.client.post(reverse('users:users_register'), self.user_register_form_data, follow=True)
    #     self.assertRedirects(response, reverse('users:users_register_form_submitted'))

    # def test_calls_send_mail(self):
    #     pass

    

class UsersRegisterFormSubmittedViewTest(TestCase):
    
    def test_uses_expected_template(self):
        response = self.client.get(reverse('users:users_register_form_submitted'))
        self.assertTemplateUsed(response, 'users/users_register_form_submitted.html')





