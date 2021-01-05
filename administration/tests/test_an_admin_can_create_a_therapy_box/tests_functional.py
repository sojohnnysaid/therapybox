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


class BaseFunctionalTest(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox()#options=options
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

        self.browser.find_element_by_id('users_admin_login_form_submit_button').click()

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

        self.browser.find_element_by_id('users_admin_login_form_submit_button').click()

        # John is redirected to the dashboard page
        assert 'Admin Dashboard' in self.browser.find_elements(By.TAG_NAME, 'h1')[0].text

    
    def test_admin_goes_to_library_box_create_page(self):
        
        # John logs in and is redirected to the dashboard page
        self.login()

        # he clicks on the inventory menu item
        self.browser.find_element_by_link_text('Inventory').click()

        # he sees the add new item button and clicks on it
        self.browser.find_element_by_link_text('+ Add new item').click()

        # he is brought to a form
        assert '+ new item' in self.browser.find_elements(By.TAG_NAME, 'h1')[0].text

        # he fills out the form
        time.sleep(1)

        # name
        input = self.browser.find_elements(By.NAME, 'name')[0]
        input.send_keys('test_name')

        # description
        input = self.browser.find_elements(By.NAME, 'description')[0]
        input.send_keys('test_description')

        time.sleep(1)
        # image
        input = self.browser.find_elements(By.NAME, 'image_1')[0]
        input.send_keys('/Users/home/Desktop/therapybox/staticfiles/test_image_1.png')
        time.sleep(2)


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

        time.sleep(3)

        # he submits the form
        self.browser.find_elements(By.ID, 'admin_create_therapy_box_template_submit')[0].click()

        time.sleep(2)

        # John is back on the inventory page
        assert 'Inventory' in self.browser.find_elements(By.TAG_NAME, 'h1')[0].text

        # he sees his new item in the inventory list
