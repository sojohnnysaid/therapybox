from unittest.case import skip
from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.core import mail
from django.urls import reverse
import re


class UsersTest(FunctionalTest):

    
    def test_user_can_register(self):

        #################################
        ####### John's User Story #######
        #################################

        # John goes to the registration page
        self.browser.get(self.live_server_url + reverse('users:register_form'))

        # he is greeted by the registration header
        assert 'Register' in self.browser.find_elements(By.TAG_NAME, 'h1')[0].text

        # John starts filling out the registration form...

        # enters his email
        input = self.browser.find_elements(By.ID, 'id_email')[0]
        assert input.get_attribute('placeholder') == 'email'
        input.send_keys('john@gmail.com')
        
        # enters his first name
        input = self.browser.find_elements(By.ID, 'id_first_name')[0]
        assert input.get_attribute('placeholder') == 'first name'
        input.send_keys('John')

        # enters his password
        input = self.browser.find_elements(By.ID, 'id_password1')[0]
        assert input.get_attribute('placeholder') == 'password'
        input.send_keys('p@assW00rd')

        # enters his password to confirm
        input = self.browser.find_elements(By.ID, 'id_password2')[0]
        assert input.get_attribute('placeholder') == 'confirm password'
        input.send_keys('p@assW00rd')

        # submits the form
        self.browser.find_elements(By.ID, 'users_register_form_submit_button')[0].click()

        # he is taken to a new page
        assert reverse('users:register_form_submitted') in self.browser.current_url

        # the page tells him an email has been sent with a confirmation link
        form_submitted_message = self.browser.find_elements(By.ID, 'users-register-form-submitted-message')[0].text
        assert 'Form submitted. Check your email to activate your new account' in form_submitted_message

        # John goes to his email...
        email = mail.outbox[0]
        assert 'Here is your activation link' in email.subject
        
        url_search = re.search(r'http://.+/users/account-activation/\?uid=.+&token=.+$', email.body)
        
        if not url_search:
            self.fail(f'Could not find url in email body:\n{email.body}')

        # the activation link is in the email body
        activate_account_url = url_search.group(0)
        assert self.live_server_url in activate_account_url

        

        #################################
        ####### Jane's User Story #######
        #################################

        # Jane goes to the registration page
        self.browser.get(self.live_server_url + reverse('users:register_form'))

        # she is greeted by the registration header
        assert 'Register' in self.browser.find_elements(By.TAG_NAME, 'h1')[0].text

        # Jane starts filling out the registration form...

        # enters her email
        input = self.browser.find_elements(By.ID, 'id_email')[0]
        assert input.get_attribute('placeholder') == 'email'
        input.send_keys('jane@gmail.com')
        
        # enters her first name
        input = self.browser.find_elements(By.ID, 'id_first_name')[0]
        assert input.get_attribute('placeholder') == 'first name'
        input.send_keys('Jane')

        # enters her password
        input = self.browser.find_elements(By.ID, 'id_password1')[0]
        assert input.get_attribute('placeholder') == 'password'
        input.send_keys('$$$p@assW00rd$$$')

        # enters her password to confirm
        input = self.browser.find_elements(By.ID, 'id_password2')[0]
        assert input.get_attribute('placeholder') == 'confirm password'
        input.send_keys('$$$p@assW00rd$$$')

        # submits the form
        self.browser.find_elements(By.ID, 'users_register_form_submit_button')[0].click()

        # she is taken to a new page
        assert reverse('users:register_form_submitted') in self.browser.current_url

        # the page tells her an email has been sent with a confirmation link
        form_submitted_message = self.browser.find_elements(By.ID, 'users-register-form-submitted-message')[0].text
        assert 'Form submitted. Check your email to activate your new account' in form_submitted_message

        # Jane goes to her email...
        email = mail.outbox[1]
        assert 'Here is your activation link' in email.subject
        
        url_search = re.search(r'http://.+/users/account-activation/\?uid=.+&token=.+$', email.body)
        
        if not url_search:
            self.fail(f'Could not find url in email body:\n{email.body}')

        # the activation link is in the email body
        activate_account_url = url_search.group(0)
        assert self.live_server_url in activate_account_url




    def test_user_can_activate_account_using_link_once(self):

        self.submit_register_user_form('John')

        # John goes to his email...
        email = mail.outbox[0]
        assert 'Here is your activation link' in email.subject
        
        url_search = re.search(r'http://.+/users/account-activation/\?uid=.+&token=.+$', email.body)
        
        if not url_search:
            self.fail(f'Could not find url in email body:\n{email.body}')

        activate_account_url = url_search.group(0)
        assert self.live_server_url in activate_account_url

        # and clicks the link
        self.browser.get(activate_account_url)
        
        # John is taken to the login page
        assert reverse('users:login') in self.browser.current_url
        navbar = self.browser.find_elements(By.CLASS_NAME, 'alert-success')[0].text
        assert 'Your account has been activated! You can now login' in navbar
    



    
    def test_user_can_reset_forgotten_password_using_email(self):

        self.user_registers_and_activates_account('John')

        # John goes to the login page
        self.browser.get(self.live_server_url + reverse('users:login'))

        # he is greeted by the login header
        assert 'Login' in self.browser.find_elements(By.TAG_NAME, 'h1')[0].text

        # John can't remember his password and notices a forgot password link
        # He clicks the link
        self.browser.find_elements(By.LINK_TEXT, 'Forgot Password? Click here!').click()

        # he is taken to the password reset form page
        assert reverse('users:password_reset_form') in self.browser.current_url

        # he is greeted by the password reset header
        assert 'Password Reset' in self.browser.find_elements(By.TAG_NAME, 'h1')[0].text

        # he sees a form with a field to enter his email
        input = self.browser.find_elements(By.ID, 'id_email')[0]
        assert input.get_attribute('placeholder') == 'email'

        # he enters his email
        input.send_keys('john@gmail.com')

        # submits the form
        self.browser.find_elements(By.ID, 'users_password_reset_form_submit_button')[0].click()

        # he is taken back to the login page
        assert reverse('users:login') in self.browser.current_url

        # the page tells him an email has been sent with a confirmation link
        form_submitted_message = self.browser.find_elements(By.ID, 'message')[0].text
        assert 'Form submitted. Check your email to reset your password' in form_submitted_message

        # John goes to his email...
        email = mail.outbox[0]
        assert 'Here is your password reset link' in email.subject
        
        url_search = re.search(r'http://.+/users/password-reset/\?uid=.+&token=.+$', email.body)
        
        if not url_search:
            self.fail(f'Could not find url in email body:\n{email.body}')

        # the activation link is in the email body
        activate_account_url = url_search.group(0)
        assert self.live_server_url in activate_account_url