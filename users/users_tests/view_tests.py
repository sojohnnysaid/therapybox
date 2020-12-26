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
from users import views, models, forms
from django.urls import reverse
from django.core import mail

from django.test import TestCase

class UsersRegisterViewTest(TestCase):
    
    def test_uses_CustomUser(self):
        view = views.UsersRegisterView()
        assert view.model == models.CustomUser
        
    def test_uses_UsersRegisterForm(self):
        response = self.client.get(reverse('users:users_register'))
        view = response.context_data['view']
        assert view.form_class == forms.UsersRegisterForm
    
    def test_uses_expected_template(self):
        response = self.client.get(reverse('users:users_register'))
        self.assertTemplateUsed(response, 'users/users_register.html')

    def test_email_sent_on_POST_request(self):
        self.client.post(reverse('users:users_register'),{'email': ['johnsmith@gmail.com'], 'first_name': ['John'], 'password1': ['p@assW0rd'], 'password2': ['p@assW0rd']})
        email = mail.outbox[0]
        assert 'Here is your activation link' in email.subject

    def test_redirects_on_POST_request(self):
        USERS_REGISTER_FORM_TEST_DATA = {
            'email': ['johnsmith@gmail.com'], 
            'first_name': ['John'], 
            'password1': ['p@assW0rd'], 
            'password2': ['p@assW0rd']}
        response = self.client.post(reverse('users:users_register'), USERS_REGISTER_FORM_TEST_DATA, follow=True)
        self.assertRedirects(response, reverse('users:users_register_form_submitted'))




class UsersRegisterFormSubmittedViewTest(TestCase):
    
    def test_uses_expected_template(self):
        response = self.client.get(reverse('users:users_register_form_submitted'))
        self.assertTemplateUsed(response, 'users/users_register_form_submitted.html')



@skip
class UsersAccountActivationView(TestCase):

    # - pull token, and url safe primary key from url query params
    # - get the user using the primary key
    # - if the token is not good guard and return error
    # - otherwise set the user is_active to True
    # - save the user
    # - pass success message 'Your account has been activated! You can now login'
    # - redirect to users_login page displaying success message

    def test_redirect_to_users_login_page(self):
        # todo url safe user pk, token
        uid = ''
        token = ''
        response = self.client.get(reverse('users:users_account_activation'), {'uid': uid, 'token': token}, follow=True)
        self.assertRedirects(response, reverse('users:users_login'))