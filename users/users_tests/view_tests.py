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
'''

from users import views, models, forms
from django.urls import reverse

from django.test import TestCase

class UsersRegisterViewTest(TestCase):
    
    def test_users_register_view_uses_testModel(self):
        view = views.UsersRegisterView()
        assert view.model == models.TestModel
        
    def test_users_register_view_uses_UsersRegisterForm(self):
        response = self.client.get(reverse('users:users_register'))
        view = response.context_data['view']
        assert view.form_class == forms.UsersRegisterForm
    
    def test_users_register_view_uses_expected_template(self):
        response = self.client.get(reverse('users:users_register'))
        self.assertTemplateUsed(response, 'users/users_register.html')




class UsersRegisterFormSubmittedViewTest(TestCase):
    
    def test_users_register_form_submitted_view_uses_expected_template(self):
        response = self.client.get(reverse('users:users_register_form_submitted'))
        self.assertTemplateUsed(response, 'users/users_register_form_submitted.html')

    
    # the page tells him an email has been sent with a confirmation link
    # form_submitted_message = self.browser.find_elements(By.ID, 'users-register-form-submitted-message')[0].text
    # assert 'Form submitted. Check your email to activate your new account' in form_submitted_message