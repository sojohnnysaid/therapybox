'''
How this class works
1. The form class describes fields to be rendered
and any custom attributes to attached to the fields. Customized fields
are generated using the widgets module. ModelForm also maps fields to 
the chosen model.

2. We can also set methods that change the behavior of our form. For
example we can declare a url to redirect to after a form has
been successfully submitted.
'''

'''
We test:
1. Can we call this form with correct fields?
2. Can we assign additional attributes to our fields widgets?
3. Can we redirect the form after the submission is successful?
'''

from django.urls import reverse
from django.test import TestCase

from users import forms

USERS_REGISTER_FORM_FIELDNAMES = ['email', 'first_name', 'password1', 'password2']
USERS_REGISTER_FORM_TEST_DATA = {'email': ['johnsmith@gmail.com'], 'first_name': ['John'], 'password1': ['p@assW0rd'], 'password2': ['p@assW0rd']}

class UsersRegisterFormTest(TestCase):

    def test_UsersRegisterForm_renders_correct_fields(self):
        form = forms.UsersRegisterForm
        field_names = list(form.base_fields.keys())
        self.assertEqual(USERS_REGISTER_FORM_FIELDNAMES, field_names)

    def test_UsersRegisterForm_fields_use_placeholder_attributes(self):
        response = self.client.get(reverse('users:users_register'))
        self.assertIn('placeholder="first name"', response.rendered_content)
        self.assertIn('placeholder="email"', response.rendered_content)
        
    def test_form_redirects_on_POST_request(self):
        response = self.client.post(reverse('users:users_register'), USERS_REGISTER_FORM_TEST_DATA, follow=True)
        self.assertRedirects(response, reverse('users:users_register_form_submitted'))