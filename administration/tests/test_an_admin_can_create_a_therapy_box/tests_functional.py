import re
import time

from unittest.case import skip

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions as Options

from django.test import LiveServerTestCase
from django.urls import reverse


class BaseFunctionalTest(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        self.browser = webdriver.Chrome(options=options)
        self.browser.implicitly_wait(15)

    def tearDown(self):
        
        self.browser.quit()




class MyFunctionalTest(BaseFunctionalTest):
    
    def test_a_story_from_the_user_perspective(self):
        pass