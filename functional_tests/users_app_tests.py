from unittest.case import skip
from .base import FunctionalTest
from selenium.webdriver.common.by import By

class UsersTest(FunctionalTest):

    @skip
    def test_user_can_create_account(self):
        # John goes to the registration page
        self.browser.get(self.live_server_url + '/register/')

        # he is greeted by the registration title and header
        assert 'Register' in self.browser.title
        assert 'Register' in self.browser.find_elements(By.TAG_NAME, 'h1')

        # he sees the form

        # enters his first name

        # enters his email

        # submits the form

        # he is taken to a new page

        # the page tells him an email has been sent with a confirmation link

        # John goes to his email and clicks the link

        # John is taken to his account page

        # There is a message that welcomes him personally

