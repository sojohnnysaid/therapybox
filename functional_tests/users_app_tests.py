from unittest.case import skip
from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.core import mail
import re


class UsersTest(FunctionalTest):

    
    def test_user_can_register(self):

        #################################
        ####### John's User Story #######
        #################################

        # John goes to the registration page
        self.browser.get(self.live_server_url + '/users/register/')

        # he is greeted by the registration title and header
        assert 'Register' in self.browser.title
        assert 'Register' in self.browser.find_elements(By.TAG_NAME, 'h1')[0].text

        # John starts filling out the registration form...

        # enters his first name
        input = self.browser.find_elements(By.ID, 'id_first_name')[0]
        assert input.get_attribute('placeholder') == 'first name'
        
        # enters his first name
        input.send_keys('John')

        # then he starts filling out his email
        input = self.browser.find_elements(By.ID, 'id_email')[0]
        assert input.get_attribute('placeholder') == 'email'
        
        # enters his email
        input.send_keys('john@gmail.com')

        # submits the form
        self.browser.find_elements(By.ID, 'users_register_form_submit_button')[0].click()

        # he is taken to a new page
        assert 'users/register-form-submitted/' in self.browser.current_url

        # the page tells him an email has been sent with a confirmation link
        form_submitted_message = self.browser.find_elements(By.ID, 'users-register-form-submitted-message')[0].text
        assert 'Form submitted. Check your email to activate your new account' in form_submitted_message

        # John goes to his email...
        email = mail.outbox[0]
        assert 'Here is your activation link' in email.subject
        
        url_search = re.search(r'http://.+/users/account/\?token=.+$', email.body)
        
        if not url_search:
            self.fail(f'Could not find url in email body:\n{email.body}')

        activate_account_url = url_search.group(0)
        assert self.live_server_url in activate_account_url

        # and clicks the link
        self.browser.get(activate_account_url)
        
        # John is taken to his account page
        assert '/users/account/' in self.browser.current_url
        navbar = self.browser.find_elements(By.TAG_NAME, 'nav')[0].text
        assert 'John' in navbar


        # There is a message that welcomes him personally
        welcome_message = self.browser.find_elements(By.CLASS_NAME, 'alert-success')[0].text
        assert 'Welcome to your new account John!' == welcome_message

        #################################
        ####### Jane's User Story #######
        #################################

        # Jane goes to the registration page
        self.browser.get(self.live_server_url + '/users/register/')

        # she is greeted by the registration title and header
        assert 'Register' in self.browser.title
        assert 'Register' in self.browser.find_elements(By.TAG_NAME, 'h1')[0].text

        # Jane starts filling out the registration form...

        # enters her first name
        input = self.browser.find_elements(By.ID, 'id_first_name')[0]
        assert input.get_attribute('placeholder') == 'first name'
        
        # enters her first name
        input.send_keys('Jane')

        # then she starts filling out her email
        input = self.browser.find_elements(By.ID, 'id_email')[0]
        assert input.get_attribute('placeholder') == 'email'
        
        # enters her email
        input.send_keys('jane@gmail.com')

        # submits the form
        self.browser.find_elements(By.ID, 'users_register_form_submit_button')[0].click()

        # she is taken to a new page
        assert 'users/register-form-submitted/' in self.browser.current_url

        # the page tells her an email has been sent with a confirmation link
        form_submitted_message = self.browser.find_elements(By.ID, 'users-register-form-submitted-message')[0].text
        assert 'Form submitted. Check your email to activate your new account' in form_submitted_message

        # Jane goes to her email...
        email = mail.outbox[0]
        assert 'Here is your activation link' in email.subject
        
        url_search = re.search(r'http://.+/users/account/\?token=.+$', email.body)
        
        if not url_search:
            self.fail(f'Could not find url in email body:\n{email.body}')

        activate_account_url = url_search.group(0)
        assert self.live_server_url in activate_account_url

        # and clicks the link
        self.browser.get(activate_account_url)
        
        # Jane is taken to her account page
        assert '/users/account/' in self.browser.current_url
        navbar = self.browser.find_elements(By.TAG_NAME, 'nav')[0].text
        assert 'Jane' in navbar


        # There is a message that welcomes her personally
        welcome_message = self.browser.find_elements(By.CLASS_NAME, 'alert-success')[0].text
        assert 'Welcome to your new account Jane!' == welcome_message