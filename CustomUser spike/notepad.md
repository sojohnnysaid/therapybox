from django.contrib.auth import get_user_model


if you reference the CustomUser model in your models.py
from django.conf import settings
settings.AUTH_USER_MODEL


1. create CustomUserManager(BaseUserManager)
and override the create_user() and create_superuser()

2. create a CustomUser(AbstractBaseUser) and include
the appropriate attributes and methods
