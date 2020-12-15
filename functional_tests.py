from selenium import webdriver
from django.test import SimpleTestCase

class FirstTest(SimpleTestCase):
    def test_first(self):
        browser = webdriver.Firefox()
        browser.get('http://localhost:8000')
        assert 'Django' in browser.title