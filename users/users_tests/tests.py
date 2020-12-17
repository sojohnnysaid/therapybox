'''
1. An HTTP request comes in for a particular URL
2. Django uses some rules to decide which view function should deal with the request (this is referred to as respolving the URL)
3. The view function processes the request and returns and HTTP response
'''

'''
We test two things:
1. Can we resolve the requested URL to a particular view function we've made?
2. Can we make this view function return HTML which will get the functional test to pass?
'''

from django.urls import reverse, resolve
from django.test import TestCase
from users.views import RegisterView


class RegisterPageTest(TestCase):

    def test_url_resolves_to_register_page_view(self):
        url = reverse('users_register')
        view = resolve(url).func.view_class
        self.assertEqual(view, RegisterView)
    