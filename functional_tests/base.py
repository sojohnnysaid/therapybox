from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from django.test import LiveServerTestCase


class FunctionalTest(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()