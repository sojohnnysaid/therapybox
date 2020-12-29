from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from django.test import LiveServerTestCase
from django.contrib.auth import get_user_model
from selenium.webdriver.common.by import By
from django.core import mail
from django.urls import reverse
import re
import time


class FunctionalTest(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)
        self.browser.implicitly_wait(15)

    def tearDown(self):
        self.browser.quit()

    
    def submit_register_user_form(self, name):
        
        self.browser.get(self.live_server_url + reverse('users:register'))
        
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


    def user_registers_and_activates_account(self, name):

        self.browser.get(self.live_server_url + reverse('users:register'))
        
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

        # goes to email...
        email = mail.outbox[0]
        
        url_search = re.search(r'http://.+/users/account-activation/\?uid=.+&token=.+$', email.body)
        
        if not url_search:
            self.fail(f'Could not find url in email body:\n{email.body}')

        activate_account_url = url_search.group(0)

        # clicks the link
        self.browser.get(activate_account_url)

    
    def user_submits_reset_password_form(self, name):

        self.user_registers_and_activates_account(name)

        #goes to the login page
        self.browser.get(self.live_server_url + reverse('users:login'))

        # can't remember password and notices a forgot password link
        # He clicks the link
        self.browser.find_elements(By.LINK_TEXT, 'Forgot Password? Click here!')[0].click()

        # he sees a form with a field to enter his email
        input = self.browser.find_elements(By.ID, 'id_email')[0]

        # he enters his email
        input.send_keys('john@gmail.com')

        # submits the form
        self.browser.find_elements(By.ID, 'users_password_reset_request_form_submit_button')[0].click()