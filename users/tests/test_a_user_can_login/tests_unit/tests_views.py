from django.test import TestCase, Client




class BaseTestCase(TestCase):

    def setUp(self):
        super().setUp()




class MyViewTest(BaseTestCase):

    def test_view_does_what_is_expected(self):
        pass