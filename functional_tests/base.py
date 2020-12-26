from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from django.test import LiveServerTestCase
from django.contrib.auth import get_user_model
from selenium.webdriver.common.by import By


class FunctionalTest(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)
        self.browser.implicitly_wait(10)

    def tearDown(self):
        self.browser.quit()

    
    def register_user(self, name):
        
        self.browser.get(self.live_server_url + '/users/register/')
        
        # enters email
        input = self.browser.find_elements(By.ID, 'id_email')[0]
        input.send_keys(f'{name}@gmail.com')
        
        # enters first name
        input = self.browser.find_elements(By.ID, 'id_first_name')[0]
        input.send_keys(f'{name}')

        # enters password
        input = self.browser.find_elements(By.ID, 'id_password1')[0]
        input.send_keys('p@assW00rd')

        # enters password to confirm
        input = self.browser.find_elements(By.ID, 'id_password2')[0]
        input.send_keys('p@assW00rd')

        # submits the form
        self.browser.find_elements(By.ID, 'users_register_form_submit_button')[0].click()