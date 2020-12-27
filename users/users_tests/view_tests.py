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

from unittest.case import skip
from unittest.mock import patch

from users import views, models, forms, services
from users.tokens import default_account_activation_token_generator as token_generator


class UsersRegisterViewTest(TestCase):

    def setUp(self):
        super().setUp()
        self.email = 'johnsmith@gmail.com'
        self.first_name = 'John'
        self.password = 'p@assW0rd'

        self.request = RequestFactory().post(reverse('users:users_register'), {
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
        assert response.url == reverse('users:users_register_form_submitted')




class SendActivationLinkTest(TestCase):

    def setUp(self):
        super().setUp()
        self.email = 'johnsmith@gmail.com'
        self.first_name = 'John'
        self.password = 'p@assW0rd'

        self.request = RequestFactory().post(reverse('users:users_register'), {
            'email': self.email,
            'first_name': self.first_name,
            'password1': self.password,
            'password2': self.password
        })

    def test_get_account_activation_email_subject(self):
        subject = services.account_activation.get_account_activation_email_subject()
        assert subject == 'Here is your activation link'

    def test_get_url_safe_user_pk(self):
        views.UsersRegisterView.as_view()(self.request)
        user = get_user_model().objects.get(email=self.email)
        url_safe_user_pk = urlsafe_base64_encode(force_bytes(user.pk))
        assert url_safe_user_pk == 'MQ'

    def test_get_account_activation_token(self):
        views.UsersRegisterView.as_view()(self.request)
        user = get_user_model().objects.get(email=self.email)
        timestamp = timezone.now()
        token_hash_value = token_generator._make_hash_value(user, timestamp)
        assert token_hash_value == (str(user.pk) + str(timestamp) + str(user.is_active))

    def test_get_account_activation_email_message(self):
        views.UsersRegisterView.as_view()(self.request)
        message = services.account_activation.test_get_account_activation_email_message(self.request)
        self.assertRegex(message, r'http://.+/users/account-activation/\?uid=.+&token=.+$')

    def test_get_account_activation_from_email(self):
        from_email = services.account_activation.get_account_activation_from_email()
        assert from_email == 'noreply@example.com'

    def test_get_account_activation_user_email(self):
        user_email = services.account_activation.get_account_activation_user_email(self.request)
        assert user_email == self.email
        
    @patch('users.services.account_activation.send_mail')
    def test_calls_send_mail(self, mock_send_mail):
        view_instance = views.UsersRegisterView.as_view()
        view_instance(self.request)
        mock_send_mail.assert_called_once()

    @patch('users.services.account_activation.send_mail')
    def test_correct_arguments_passed_to_send_mail(self, mock_send_mail):
        view_instance = views.UsersRegisterView.as_view()
        view_instance(self.request)
        link = mock_send_mail.call_args[0][1]
        url = re.search(r'http://.+/users/account-activation/\?uid=.+&token=.+$', link)
        mock_send_mail.assert_called_once_with(
            'Here is your activation link',
            url.group(0),
            'noreply@example.com',
            ['johnsmith@gmail.com'],
            fail_silently=False,
        )




#TODO
class UsersAccountActivationViewTest(TestCase):
    pass

#TODO
class UsersLoginViewTest(TestCase):
    pass