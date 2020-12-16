import django
from django.urls import reverse
from selenium.webdriver.common.by import By

from .base import FunctionalTest


class DjangoInstallationTest(FunctionalTest):

    def test_django_is_correct_version_number(self):
        assert django.get_version() == '3.1.4'

    def test_shows_success_page(self):
        # django install is working properly and shows welcome page
        self.browser.get(self.live_server_url + reverse('debug'))
        assert 'Django' in self.browser.title
        assert 'The install worked successfully! Congratulations!' in self.browser.find_elements(By.TAG_NAME, 'h2')[1].text
        header = self.browser.find_elements(By.TAG_NAME, 'header')[0]
        assert 'u-clearfix' in header.get_attribute('class')