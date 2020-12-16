from unittest.case import skip
from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class UsersTest(FunctionalTest):

    @skip
    def test_user_can_create_account(self):
        # John goes to the registration page
        self.browser.get(self.live_server_url + '/register/')

        # he is greeted by the registration title and header
        assert 'Register' in self.browser.title
        assert 'Register' in self.browser.find_elements(By.TAG_NAME, 'h1')[0].text

        # he fills out the registration form...
        # enters his first name
        input = self.browser.find_elements(By.ID, 'user-registration-form-first-name-field')[0]
        assert input.get_attribute('placeholder') == 'first name'
        input.send_keys('John')

        # enters his email
        input = self.browser.find_elements(By.ID, 'user-registration-form-email-field')[0]
        assert input.get_attribute('placeholder') == 'email'
        input.send_keys('john@gmail.com')

        # submits the form
        input.submit()

        # he is taken to a new page

        # the page tells him an email has been sent with a confirmation link

        # John goes to his email and clicks the link

        # John is taken to his account page

        # There is a message that welcomes him personally

