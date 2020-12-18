'''
1. An HTTP request comes in for a particular URL
2. Django uses some rules to decide which view function should deal with the request (this is referred to as respolving the URL)
3. The view function processes the request and returns and HTTP response
'''

'''
We test two things:
1. Can we resolve the requested URL to a particular view function we've made?
2. Can we make this view function return HTML which will get the functional test to pass?
'''

from django.urls import reverse
from django.test import TestCase

REGISTER_FORM_TEST_DATA = {'first_name': 'John', 'email': 'sojohnnysaid@gmail.com'}

class UsersRegisterPageTest(TestCase):
        
    def test_uses_register_template(self):
        response = self.client.get(reverse('users_register'))
        self.assertTemplateUsed(response, 'users/users_register.html')

    def test_register_view_uses_UsersRegisterForm_form_class(self):
        response = self.client.get(reverse('users_register'))
        view_class = response.context_data['view']
        users_register_form_class = UsersRegisterForm()
        assert view.form_class == users_register_form_class


    def test_form_redirects_on_POST_request(self):
        response = self.client.post(reverse('users_register'), REGISTER_FORM_TEST_DATA, follow=True)
        print(response.__dict__)