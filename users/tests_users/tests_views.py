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

import re
from django.test.testcases import TestCase
from django.urls import reverse, reverse_lazy
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils import timezone
from django.core import mail
from django.test import Client

from unittest.case import skip
from unittest.mock import patch

from users import views, models, forms, services
from users.tests_users import base
from users.tokens import default_account_activation_token_generator as token_generator


class UsersRegisterViewTest(TestCase):

    def setUp(self):
        super().setUp()
        self.email = 'johnsmith@gmail.com'
        self.first_name = 'John'
        self.password = 'p@assW0rd'

        self.request = RequestFactory().post(reverse('users:register'), {
            'email': self.email,
            'first_name': self.first_name,
            'password1': self.password,
            'password2': self.password
        })

    def tearDown(self):
        return super().tearDown()

    def test_uses_CustomUser(self):
        assert views.UsersRegisterView.model == models.CustomUser
        
    def test_uses_UsersRegisterForm(self):
        assert views.UsersRegisterView.form_class == forms.UsersRegisterForm

    def test_uses_expected_template(self):
        assert views.UsersRegisterView.template_name == 'users/users_register.html'

    def test_redirects_on_post_request(self):
        view_instance = views.UsersRegisterView.as_view()
        response = view_instance(self.request)
        assert response.url == reverse('users:register_form_submitted')




class UsersRegisterFormSubmittedViewTest(TestCase):
    
    def test_get_request_returns_expected_html(self):
        response = Client().get(reverse('users:register_form_submitted'))
        self.assertInHTML('Form Submitted', response.rendered_content)




class SendActivationLinkTest(TestCase):

    def setUp(self):
        super().setUp()
        self.email = 'johnsmith@gmail.com'
        self.first_name = 'John'
        self.password = 'p@assW0rd'

        self.request = RequestFactory().post(reverse('users:register'), {
            'email': self.email,
            'first_name': self.first_name,
            'password1': self.password,
            'password2': self.password
        })
        
    @patch('users.services.send_mail')
    def test_calls_send_mail_service(self, mock_send_mail):
        views.UsersRegisterView.as_view()(self.request)
        mock_send_mail.assert_called_once()

    @patch('users.services.send_mail')
    def test_correct_arguments_passed_to_send_mail_service(self, mock_send_mail):
        views.UsersRegisterView.as_view()(self.request)
        link = mock_send_mail.call_args[0][1]
        url = re.search(r'http://.+/users/account-activation/\?uid=.+&token=.+$', link)
        mock_send_mail.assert_called_once_with(
            'Here is your activation link',
            url.group(0),
            'noreply@example.com',
            ['johnsmith@gmail.com'],
            fail_silently=False,
        )



class UsersAccountActivationViewTest(TestCase):

    # use Client instead of RequestFactory in tests because messages will not work otherwise

    def setUp(self):
        super().setUp()
        self.email = 'johnsmith@gmail.com'
        self.first_name = 'John'
        self.password = 'p@assW0rd'

        self.register_request = RequestFactory().post(reverse('users:register'), {
            'email': self.email,
            'first_name': self.first_name,
            'password1': self.password,
            'password2': self.password
        })

        views.UsersRegisterView.as_view()(self.register_request)
        email = mail.outbox[0]
        url_search = re.search(r'http://.+/users/account-activation/\?uid=.+&token=.+$', email.body)
        self.account_activation_link = url_search.group(0)

    @patch('users.views.services')
    def test_calls_activate_user_service(self, mock_services):
        Client().get(self.account_activation_link)
        mock_services.activate_user.assert_called_once()

    @patch('users.views.services')
    def test_correct_arguments_passed_to_activate_user_service(self, mock_services):
        response = Client().get(self.account_activation_link)
        initial_request = response.wsgi_request
        mock_services.activate_user.assert_called_once_with(initial_request)

    def test_redirect(self):
        response = Client().get(self.account_activation_link)
        self.assertRedirects(response, reverse('users:login'))



class UsersLoginViewTest(TestCase):

    def test_returns_expected_template(self):
        response = Client().get(reverse('users:login'))
        self.assertTemplateUsed(response, 'users/users_login.html')
    
    def test_get_request_returns_expected_html(self):
        response = Client().get(reverse('users:login'))
        self.assertInHTML('Login Page', response.rendered_content)




class UsersPasswordResetRequestViewTest(base.UsersBaseTestCase):

    def test_get_request_returns_expected_html(self):
        response = Client().get(reverse('users:password_reset_request'))
        self.assertTemplateUsed(response, 'users/users_password_reset_request.html')

    def test_uses_expected_form_class(self):
        response = Client().get(reverse('users:password_reset_request'))
        self.assertIsInstance(response.context_data['form'], forms.UsersPasswordResetRequestForm)

    @patch('users.views.services')
    def test_calls_send_password_reset_link_service_with_expected_arguments(self, mocked_services):
        user = self.create_test_user('John')
        response = Client().post(reverse('users:password_reset_request'), {'email': 'John@gmail.com'})
        request = response.wsgi_request
        mocked_services.send_password_reset_link.assert_called_once_with(request, user)

    def test_redirects_on_post_success(self):
        user = self.create_test_user('John')
        response = Client().post(reverse('users:password_reset_request'), {'email': 'John@gmail.com'})
        self.assertRedirects(response, reverse('users:login'))