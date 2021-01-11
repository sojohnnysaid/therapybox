import re
import time

from unittest.case import skip

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions as Options

from django.test import LiveServerTestCase
from django.urls import reverse
from django.conf import settings as conf_settings
from django.core import mail


class BaseFunctionalTest(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        self.browser = webdriver.Chrome(options=options)
        self.browser.implicitly_wait(15)

    def tearDown(self):
        
        self.browser.quit()




class UserRegistration(BaseFunctionalTest):
    
    def test_a_facility_can_register(self):
        # John goes to the registration page
        self.browser.get(self.live_server_url + reverse('users:register'))

        # he is greeted by the registration header
        assert 'Registration' in self.browser.find_elements(By.TAG_NAME, 'h1')[0].text

        # John starts filling out the registration form...

        # email
        input = self.browser.find_elements(By.NAME, 'email')[0]
        input.send_keys('john@gmail.com')

        # password
        input = self.browser.find_elements(By.NAME, 'password1')[0]
        input.send_keys('p@assW00rd')

        # password to confirm
        input = self.browser.find_elements(By.NAME, 'password2')[0]
        input.send_keys('p@assW00rd')

        # facility_name
        input = self.browser.find_elements(By.NAME, 'facility_name')[0]
        input.send_keys('facility_name')

        # company_name
        input = self.browser.find_elements(By.NAME, 'company_name')[0]
        input.send_keys('company_name')

        # phone_number
        input = self.browser.find_elements(By.NAME, 'phone_number')[0]
        input.send_keys('phone_number')

        # point_of_contact
        input = self.browser.find_elements(By.NAME, 'point_of_contact')[0]
        input.send_keys('point_of_contact')



        # billing
        # billing_address_line_1
        input = self.browser.find_elements(By.NAME, 'billing_address_line_1')[0]
        input.send_keys('billing_address_line_1')

        # billing_address_line_2
        input = self.browser.find_elements(By.NAME, 'billing_address_line_2')[0]
        input.send_keys('billing_address_line_2')

        # billing_suburb
        input = self.browser.find_elements(By.NAME, 'billing_suburb')[0]
        input.send_keys('billing_suburb')

        # billing_city
        input = self.browser.find_elements(By.NAME, 'billing_city')[0]
        input.send_keys('billing_city')

        # billing_postcode
        input = self.browser.find_elements(By.NAME, 'billing_postcode')[0]
        input.send_keys('billing_postcode')




        # shipping_address_line_1
        input = self.browser.find_elements(By.NAME, 'shipping_address_line_1')[0]
        input.send_keys('address_line_1')

        # shipping_address_line_2
        input = self.browser.find_elements(By.NAME, 'shipping_address_line_2')[0]
        input.send_keys('address_line_2')

        # shipping_suburb
        input = self.browser.find_elements(By.NAME, 'shipping_suburb')[0]
        input.send_keys('suburb')

        # shipping_city
        input = self.browser.find_elements(By.NAME, 'shipping_city')[0]
        input.send_keys('city')

        # shipping_postcode
        input = self.browser.find_elements(By.NAME, 'shipping_postcode')[0]
        input.send_keys('postcode')





        # shipping_region
        input = self.browser.find_element_by_xpath("//select[@name='shipping_region']/option[text()='Region 1']")
        input.click()

        # agreed_to_terms_and_conditions
        input = self.browser.find_elements_by_xpath(".//*[contains(text(), 'Agreed to terms and conditions')]")[0]
        input.click()

        # submits the form
        self.browser.find_elements(By.ID, 'form_submit_button_register')[0].click()

        # he is taken to a new page
        assert str(conf_settings.MY_ABSTRACT_USER_SETTINGS['users_messages_page']) in self.browser.current_url

        # the page tells him an email has been sent with a confirmation link
        form_submitted_message = self.browser.find_elements(By.CLASS_NAME, 'message')[0].text
        assert 'Form submitted. Check your email to activate your new account' in form_submitted_message

        # John goes to his email...
        email = mail.outbox[0]
        assert 'Here is your activation link' in email.subject
        
        url_search = re.search(r'http://.+/account-activation/\?uid=.+&token=.+$', email.body)
        
        if not url_search:
            self.fail(f'Could not find url in email body:\n{email.body}')

        # the activation link is in the email body
        activate_account_url = url_search.group(0)
        assert self.live_server_url in activate_account_url
