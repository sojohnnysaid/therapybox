from django.test import TestCase, Client




class BaseTestCase(TestCase):

    def setUp(self):
        super().setUp()




class MyUrlTest(BaseTestCase):

    def test_url_does_what_is_expected(self):
        pass