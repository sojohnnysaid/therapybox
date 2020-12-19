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

from unittest.case import skip
from django.urls import reverse
from django.test import TestCase

from users import views, forms, models

USERS_REGISTER_FORM_TEST_DATA = {'first_name': 'John', 'email': 'sojohnnysaid@gmail.com'}


class UsersRegisterViewTest(TestCase):
    
    def test_users_register_view_uses_testModel(self):
        view = views.UsersRegisterView()
        assert view.model == models.TestModel
        
    def test_users_register_view_uses_UsersRegisterForm(self):
        response = self.client.get(reverse('users:users_register'))
        view = response.context_data['view']
        assert view.form_class == forms.UsersRegisterForm
    
    def test_users_register_view_uses_register_template(self):
        response = self.client.get(reverse('users:users_register'))
        self.assertTemplateUsed(response, 'users/users_register.html')

    
class UsersRegisterFormTest(TestCase):

    def test_user_register_form_accepts_valid_data(self):
        form = forms.UsersRegisterForm(USERS_REGISTER_FORM_TEST_DATA)
        self.assertTrue(form.is_valid())
    
    def test_form_redirects_on_POST_request(self):
        response = self.client.post(reverse('users:users_register'), USERS_REGISTER_FORM_TEST_DATA, follow=True)
        self.assertRedirects(response, reverse('users:users_register_form_submitted'))
    

class UsersModelTest(TestCase):

    def test_string_is_email(self):
        user_object = models.TestModel(first_name='John', email='sojohnnysaid@gmail.com')
        self.assertEqual(str(user_object), user_object.email)