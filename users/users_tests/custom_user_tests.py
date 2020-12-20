'''
steps required to create a custom user model:
1. add AUTH_USER_MODEL = 'users.CustomUser' to therapybox.settings
2. Register the model in the users app admin.py
3. create the model inheriting from django.contrib.auth.models.AbstractUser

3. create a custom user manager
4. define the create_user and create_superuser methods

'''