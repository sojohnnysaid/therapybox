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

from django.test.testcases import LiveServerTestCase
from django.urls import reverse
from django.test import TestCase
from django.test import RequestFactory
from django.contrib.auth import get_user_model

from unittest.mock import patch

from users import views, models, forms

class UsersRegisterViewTest(LiveServerTestCase):

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

    @patch('users.views.send_activation_link')
    def test_on_POST_send_activation_link_called(self, mock_send_activation_link):
        view_instance = views.UsersRegisterView.as_view()
        response = view_instance(self.request)
        user = get_user_model().objects.get(email=self.email)
        mock_send_activation_link.assert_called_once()

    @patch('users.views.send_activation_link')
    def test_on_POST_correct_arguments_passed_to_send_activation_link(self, mock_send_activation_link):
        view_instance = views.UsersRegisterView.as_view()
        response = view_instance(self.request)
        user = get_user_model().objects.get(email=self.email)
        mock_send_activation_link.assert_called_once_with(self.request, user)


    

    

class UsersRegisterFormSubmittedViewTest(TestCase):
    
    def test_uses_expected_template(self):
        response = self.client.get(reverse('users:users_register_form_submitted'))
        self.assertTemplateUsed(response, 'users/users_register_form_submitted.html')





