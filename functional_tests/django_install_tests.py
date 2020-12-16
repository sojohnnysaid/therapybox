from django.urls import reverse
from .base import FunctionalTest
from selenium.webdriver.common.by import By
import django


class DjangoInstallationTest(FunctionalTest):

    def test_django_is_correct_version_number(self):
        assert django.get_version() == '3.1.4'

    def test_shows_success_page(self):
        # django install is working properly and shows welcome page
        self.browser.get(self.live_server_url + reverse('debug'))
        assert 'Django' in self.browser.title
        assert 'django' in self.browser.find_elements(By.TAG_NAME, 'h2')[0].text