from django.test import Client
from django.urls import reverse
response = Client().get(reverse('users_register'))
response.context_data



from django.test import Client
from django.urls import reverse
USERS_REGISTER_FORM_TEST_DATA = {'first_name': 'John', 'email': 'sojohnnysaid@gmail.com'}
response = Client().post(reverse('users:users_register'), USERS_REGISTER_FORM_TEST_DATA, follow=True)
view = response.context_data['view']
form = response.context_data['form']
view.form_valid(form)



from users import forms
USERS_REGISTER_FORM_TEST_DATA = {'first_name': 'John', 'email': 'sojohnnysaid@gmail.com'}
form = forms.UsersRegisterForm(USERS_REGISTER_FORM_TEST_DATA)