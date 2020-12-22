'''
1. create CustomUserManager(BaseUserManager)
and override the create_user() and create_superuser()

2. add AUTH_USER_MODEL to settings.py
('users.CustomUser')

3. create a CustomUser(AbstractBaseUser) and include
the appropriate attributes and methods
(* a migration must be created once this is completed)

4. create a form for the front end
that inherits from UserCreationForm

5. on the admin.py side we create:
 - UserCreationForm
 - UserChangeForm
 - UserAdmin (to configure the way the admin panel looks)

6. Register the CustomUser and UserAdmin
in admin.py
'''

from django.test import TestCase
from users.managers import CustomUserManager

from users import models, forms, admin
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib import admin as django_admin

TEST_CUSTOM_USER_MODEL_FIRST_NAME = 'John'
TEST_CUSTOM_USER_MODEL_EMAIL = 'sojohnnysaid@gmail.com'

class CustomUserTest(TestCase):
    
    # CustomUserManager
    def test_CustomUserManager_has_create_methods(self):
        assert 'create_user' in dir(CustomUserManager)
        assert 'create_superuser' in dir(CustomUserManager)

    def test_AUTH_USER_MODEL_in_settings(self):
        assert settings.AUTH_USER_MODEL == 'users.CustomUser'

    def test_CustomUserManager_is_called_in_CustomUser_object_attribute(self):
        assert get_user_model().objects == CustomUserManager()

    # CustomUser model
    def test_CustomUser_object_created_properly(self):
        user_object = get_user_model()(first_name=TEST_CUSTOM_USER_MODEL_FIRST_NAME, email=TEST_CUSTOM_USER_MODEL_EMAIL)
        self.assertEqual(user_object.first_name, TEST_CUSTOM_USER_MODEL_FIRST_NAME)
        self.assertEqual(user_object.email, TEST_CUSTOM_USER_MODEL_EMAIL)

    def test_CustomUser_object_persists_in_database_when_saved(self):
        user_object = get_user_model()(first_name=TEST_CUSTOM_USER_MODEL_FIRST_NAME, email=TEST_CUSTOM_USER_MODEL_EMAIL)
        user_object.save()
        self.assertEqual(1, len(get_user_model().objects.all()))

    def test_str_of_user_object_is_email(self):
        user_object = get_user_model()(first_name=TEST_CUSTOM_USER_MODEL_FIRST_NAME, email=TEST_CUSTOM_USER_MODEL_EMAIL)
        self.assertEqual(str(user_object), user_object.email)

    # Custom UserRegisterForm
    def test_custom_user_register_form_uses_CustomUser(self):
        assert forms.UsersRegisterForm()._meta.__dict__['model'] == get_user_model()

    # Admin pages
    def test_UserCreationForm_uses_CustomUser(self):
        assert admin.UserCreationForm()._meta.__dict__['model'] == get_user_model()

    def test_UserChangeForm_uses_CustomUser(self):
        assert admin.UserChangeForm()._meta.__dict__['model'] == get_user_model()

    def test_UserAdmin_uses_Custom_Forms(self):
        assert admin.UserAdmin.__dict__['form'] == admin.UserChangeForm
        assert admin.UserAdmin.__dict__['add_form'] == admin.UserCreationForm

    def test_custom_admin_registered(self):
        registry = django_admin.site._registry
        assert get_user_model() in registry
        self.assertIsInstance(registry[get_user_model()], admin.UserAdmin)