'''
How this class works
1. Each Model is a Python class that subclasses djangodh.models.Model
2. Each attribute of the model represents a database field
3. With all of this, Django gives you an automatically-generated db API

1. We declare attributes that represent each database field
2. For each attribute we use models.[fieldtype] to choose the fieldtype
3. within the [fieldtype] method we pass keyword arguments to set
 - data type in the database
 - HTML widget to be used
 - some minimal validation requirements
 - in some cases the model that share a relationship (many to many etc)
4. assign methods that add 'row-level' functionality (deal with a single object)
5. We can use the Manager that exists on all Django model classes by using the name objects
(example myModel.objects.all() - returns all myModel objects. Call this on the class itself)
'''

'''
We test:
1. Can we create an object with the correct fields?
2. If we save the object will it persist in the database?
3. Does the string represention of the object return the field we expect?
'''

from django.test import TestCase
from users import models

CUSTOM_USER_MODEL_FIRST_NAME = 'John'
CUSTOM_USER_MODEL_EMAIL = 'sojohnnysaid@gmail.com'

class CustomUserTest(TestCase):

    def test_CustomUser_object_created_properly(self):
        user_object = models.CustomUser(first_name=CUSTOM_USER_MODEL_FIRST_NAME, email=CUSTOM_USER_MODEL_EMAIL)
        self.assertEqual(user_object.first_name, 'John')
        self.assertEqual(user_object.email, 'sojohnnysaid@gmail.com')

    def test_CustomUser_object_persists_in_database_when_saved(self):
        user_object = models.CustomUser(first_name=CUSTOM_USER_MODEL_FIRST_NAME, email=CUSTOM_USER_MODEL_EMAIL)
        user_object.save()
        self.assertEqual(1, len(models.CustomUser.objects.all()))

    def test_str_of_user_object_is_email(self):
        user_object = models.CustomUser(first_name=CUSTOM_USER_MODEL_FIRST_NAME, email=CUSTOM_USER_MODEL_EMAIL)
        self.assertEqual(str(user_object), user_object.email)