import re
import time

from unittest.case import skip

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from django.test import LiveServerTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.conf import settings as conf_settings


class BaseFunctionalTest(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)
        self.browser.implicitly_wait(15)
        
        self.email = 'test@gmail.com'
        self.password = 'password'
        self.user = get_user_model().objects.create_superuser(self.email, self.password)

    def tearDown(self):
        self.browser.quit()

    
    def login(self):
        # John goes to the registration page
        self.browser.get(self.live_server_url + reverse('users:admin_login'))

        # John starts logging in...

        # email
        input = self.browser.find_elements(By.NAME, 'username')[0]
        input.send_keys(self.email)

        # password
        input = self.browser.find_elements(By.NAME, 'password')[0]
        input.send_keys(self.password)

        self.browser.find_element_by_id('form_submit_button_admin_login').click()

        # John is redirected to the dashboard page
        assert 'Admin Dashboard' in self.browser.find_elements(By.TAG_NAME, 'h1')[0].text




class AdminLogsInAndCreatesTherapyBoxInstance(BaseFunctionalTest):
    
    def test_admin_logs_in(self):
        # John goes to the registration page
        self.browser.get(self.live_server_url + reverse('users:admin_login'))

        # John starts logging in...

        # email
        input = self.browser.find_elements(By.NAME, 'username')[0]
        input.send_keys(self.email)

        # password
        input = self.browser.find_elements(By.NAME, 'password')[0]
        input.send_keys(self.password)

        self.browser.find_element_by_id('form_submit_button_admin_login').click()

        # John is redirected to the dashboard page
        assert 'Admin Dashboard' in self.browser.find_elements(By.TAG_NAME, 'h1')[0].text

    
    def test_admin_goes_to_library_box_create_page(self):
        
        # John logs in and is redirected to the dashboard page
        self.login()

        # he clicks on the Catalog menu item
        self.browser.find_element_by_link_text('Catalog').click()

        # he sees the add new item button and clicks on it
        self.browser.find_element_by_link_text('+ Add new item').click()

        # he is brought to a form
        assert 'Create a Therapy Box Template' in self.browser.find_elements(By.TAG_NAME, 'h1')[0].text

        # he fills out the form

        # name
        input = self.browser.find_elements(By.NAME, 'name')[0]
        input.send_keys('test_name')

        # description
        input = self.browser.find_elements(By.NAME, 'description')[0]
        input.send_keys('test_description')

        # image_1
        input = self.browser.find_elements(By.NAME, 'image_1')[0]
        input.send_keys(f'{conf_settings.BASE_DIR}/static/test_uploads/test_image_1.png')

        # image_2
        input = self.browser.find_elements(By.NAME, 'image_2')[0]
        input.send_keys(f'{conf_settings.BASE_DIR}/static/test_uploads/test_image_1.png')

        # image_3
        input = self.browser.find_elements(By.NAME, 'image_3')[0]
        input.send_keys(f'{conf_settings.BASE_DIR}/static/test_uploads/test_image_1.png')

        # tags
        input = self.browser.find_elements(By.NAME, 'tags')[0]
        input.send_keys('test_tags')

        # length
        input = self.browser.find_elements(By.NAME, 'length')[0]
        input.send_keys('test_length')

        # height
        input = self.browser.find_elements(By.NAME, 'height')[0]
        input.send_keys('test_height')

        # depth
        input = self.browser.find_elements(By.NAME, 'depth')[0]
        input.send_keys('test_depth')

        # weight
        input = self.browser.find_elements(By.NAME, 'weight')[0]
        input.send_keys('test_weight')

        # he submits the form
        self.browser.find_elements(By.ID, 'form_submit_button_create_therapy_box_template')[0].click()


        # John is back on the catalog page
        assert 'Catalog' in self.browser.find_elements(By.TAG_NAME, 'h1')[0].text
