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
Does the string represention of the object return the field we expect?
'''

from django.test import TestCase
from users.models import CustomUser
from django.contrib.auth.models import Permission


class CustomUserTest(TestCase):

    def test_str_of_user_object_is_email(self):
        custom_user_instance = CustomUser.objects.create_user(email='test@gmail.com', password='pP@assw0rd')
        self.assertEqual(str(custom_user_instance), custom_user_instance.email)

    def test_created_user_has_no_permissions(self):
        user_instance = CustomUser.objects.create_user(email='test@gmail.com', password='pP@assw0rd')
        user_permissions = user_instance.get_user_permissions()
        self.assertSetEqual(user_permissions, set())

    def test_created_super_user_has_all_permissions(self):
        permissions = Permission.objects.all()
        permissions_list = [perm.content_type.app_label + '.' + perm.codename for perm in permissions]
        user_instance = CustomUser.objects.create_superuser(email='test@gmail.com', password='pP@assw0rd')
        user_permissions = list(user_instance.get_user_permissions())
        self.assertSetEqual(set(user_permissions), set(permissions_list))