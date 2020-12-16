from selenium import webdriver
from django.test import LiveServerTestCase
from django.urls import reverse

class FirstTest(LiveServerTestCase):

    def test_first(self):
    # our django install is working properly
        browser = webdriver.Firefox()
        browser.get(self.live_server_url + reverse('debug'))
        assert 'Django' in browser.title
