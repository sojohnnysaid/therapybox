'''
1. create CustomUserManager(BaseUserManager)
and override the create_user() and create_superuser()

2. create a CustomUser(AbstractBaseUser) and include
the appropriate attributes and methods

3. create a form for the front end
that inherits from UserCreationForm

4. on the admin.py side we create:
 - UserCreationForm
 - UserChangeForm
 - UserAdmin (to configure the way the admin panel looks)

5. Register the CustomUser and UserAdmin
in admin.py

6. add AUTH_USER_MODEL to settings.py
('users.CustomUser')
'''

from django.test import TestCase
from users.managers import CustomUserManager

class CustomUserTest(TestCase):
    
    def test_CustomUserManager_has_create_user_method(self):
        assert 'create_user' in dir(CustomUserManager)
