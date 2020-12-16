from django.urls import reverse
from .base import FunctionalTest

class DjangoInstallationTest(FunctionalTest):

    def test_shows_success_page(self):
        # django install is working properly and shows welcome page
        self.browser.get(self.live_server_url + reverse('debug'))
        assert 'Django' in self.browser.title

