from django.test import TestCase, Client




class BaseTestCase(TestCase):

    def setUp(self):
        super().setUp()




class AdminTests(TestCase):

    def test_admin_does_what_is_expected(self):
        pass