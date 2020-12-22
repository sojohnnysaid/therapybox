from django.contrib.auth import get_user_model


if you reference the CustomUser model in your models.py
from django.conf import settings
settings.AUTH_USER_MODEL


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
