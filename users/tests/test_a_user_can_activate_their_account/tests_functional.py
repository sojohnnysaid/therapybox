import re
import time

from unittest.case import skip

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from django.test import LiveServerTestCase
from django.urls import reverse
from django.core import mail
from django.conf import settings as conf_settings


class BaseFunctionalTest(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        self.browser = webdriver.Firefox(options=options)
        self.browser.implicitly_wait(15)


    def tearDown(self):
        self.browser.quit()


    def submit_register_user_form(self, name):
        
        # this is the test_a_user_can_register test_funcional.py code. Do not change it directly
        # just copy the test code from the other file!
        self.browser.get(self.live_server_url + reverse('users:register'))
        input = self.browser.find_elements(By.NAME, 'email')[0]
        input.send_keys('john@gmail.com')
        input = self.browser.find_elements(By.NAME, 'password1')[0]
        input.send_keys('p@assW00rd')
        input = self.browser.find_elements(By.NAME, 'password2')[0]
        input.send_keys('p@assW00rd')
        input = self.browser.find_elements(By.NAME, 'facility_name')[0]
        input.send_keys('facility_name')
        input = self.browser.find_elements(By.NAME, 'company_name')[0]
        input.send_keys('company_name')
        input = self.browser.find_elements(By.NAME, 'phone_number')[0]
        input.send_keys('phone_number')
        input = self.browser.find_elements(By.NAME, 'point_of_contact')[0]
        input.send_keys('point_of_contact')
        input = self.browser.find_elements(By.NAME, 'address_line_1')[0]
        input.send_keys('address_line_1')
        input = self.browser.find_elements(By.NAME, 'address_line_2')[0]
        input.send_keys('address_line_2')
        input = self.browser.find_elements(By.NAME, 'suburb')[0]
        input.send_keys('suburb')
        input = self.browser.find_elements(By.NAME, 'city')[0]
        input.send_keys('city')
        input = self.browser.find_elements(By.NAME, 'postcode')[0]
        input.send_keys('postcode')
        input = self.browser.find_element_by_xpath("//select[@name='shipping_region']/option[text()='Region 1']")
        input.click()
        input = self.browser.find_elements_by_xpath(".//*[contains(text(), 'Agreed to terms and conditions')]")[0]
        input.click()
        self.browser.find_elements(By.ID, 'users_register_form_submit_button')[0].click()




class UserCanActivateAccountUsingLinkOnceTest(BaseFunctionalTest):
    
    def test_John_can_activate_account_using_link_once(self):
        
        self.submit_register_user_form('John')

        # John goes to his email...
        email = mail.outbox[0]
        assert 'Here is your activation link' in email.subject

        url_search = re.search(r'http://.+/account-activation/\?uid=.+&token=.+$', email.body)

        if not url_search:
            self.fail(f'Could not find url in email body:\n{email.body}')

        activate_account_url = url_search.group(0)
        assert self.live_server_url in activate_account_url

        # and clicks the link
        self.browser.get(activate_account_url)
        
        # John is taken to the home page
        assert str(conf_settings.MY_ABSTRACT_USER_SETTINGS['users_messages_page']) in self.browser.current_url
        success_message = self.browser.find_elements(By.CLASS_NAME, 'message')[0].text
        assert 'Your account has been activated! You can now login' in success_message