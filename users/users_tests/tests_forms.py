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

from django.test import TestCase
from django.urls import reverse

from users import forms, models


class UsersRegisterFormTest(TestCase):

    def test_uses_CustomUser_model(self):
        form = forms.UsersRegisterForm
        self.assertEqual(form._meta.model, models.CustomUser)

    def test_renders_correct_fields(self):
        form = forms.UsersRegisterForm
        field_names = list(form.base_fields.keys())
        self.assertEqual(['email', 'first_name', 'password1', 'password2'], field_names)

    def test_fields_use_placeholder_attributes(self):
        response = self.client.get(reverse('users:register'))
        self.assertIn('placeholder="first name"', response.rendered_content)
        self.assertIn('placeholder="email"', response.rendered_content)
        
    

class UsersPasswordResetRequestFormTest(TestCase):

    def test_renders_correct_fields(self):
        form = forms.UsersPasswordResetRequestForm
        field_names = list(form.base_fields.keys())
        self.assertEqual(['email'], field_names)

    def test_fields_use_placeholder_attributes(self):
        response = self.client.get(reverse('users:password_reset_request'))
        self.assertIn('placeholder="email"', response.rendered_content)