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

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from users import forms, models
from users.tests_users import base


class UsersRegisterFormTest(base.UsersBaseTestCase):

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
        
    

class UsersPasswordResetRequestFormTest(base.UsersBaseTestCase):

    def test_renders_expected_instance(self):
        form = forms.UsersPasswordResetRequestForm()
        self.assertIsInstance(form, forms.UsersPasswordResetRequestForm)

    def test_has_correct_fields(self):
        form = forms.UsersPasswordResetRequestForm()
        self.assertEqual(list(form.fields.keys()), ['email'])

    def test_form_converts_email_to_lowercase(self):
        self.create_test_user('John')
        form = forms.UsersPasswordResetRequestForm({'email': 'JOHN@GMAIL.com'})
        form.cleaned_data = {'email':'JOHN@GMAIL.com'}
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['email'], 'john@gmail.com')

    def test_form_email_field_raises_validation_error_when_user_not_found(self):
        self.create_test_user('John')
        self.assertFalse(get_user_model().objects.filter(email='wrong@gmail.com').exists())
        form = forms.UsersPasswordResetRequestForm({'email': 'wrong@gmail.com'})
        self.assertEqual(form.errors['email'], ['No account associated with the email you submitted!'])