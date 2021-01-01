from platform import python_version

import django
from django.urls import reverse
from django.test import LiveServerTestCase, SimpleTestCase

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


class BaseFunctionalTest(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)
        self.browser.implicitly_wait(15)

    def tearDown(self):
        self.browser.quit()




class DjangoInstallationTest(SimpleTestCase):

    def test_python_is_correct_version_number(self):
        assert '3.8' in python_version()

    def test_django_is_correct_version_number(self):
        assert django.get_version() == '3.1.4'




class DjangoInstallationTest(BaseFunctionalTest):

    def test_python_is_correct_version_number(self):
        assert '3.8' in python_version()

    def test_django_is_correct_version_number(self):
        assert django.get_version() == '3.1.4'

    def test_shows_success_page(self):
        # django install is working properly and shows welcome page
        self.browser.get(self.live_server_url + reverse('debug'))
        assert 'Django' in self.browser.title
        assert 'The install worked successfully! Congratulations!' in self.browser.find_elements(By.TAG_NAME, 'h2')[1].text
        header = self.browser.find_elements(By.TAG_NAME, 'header')[0]
        assert 'u-clearfix' in header.get_attribute('class')