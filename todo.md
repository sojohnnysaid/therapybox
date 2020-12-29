✅ TODO LIST 
[✅] explain from users perspective
[✅] explain from framework perspective
[] write unit tests
[] pass functional test


current functional test expected failure to pass:
    # he is taken to the password reset form page
    assert reverse('users:password_reset_request') in self.browser.current_url

    # he is greeted by the password reset header
    assert 'Password Reset' in self.browser.find_elements(By.TAG_NAME, 'h1')[0].text


quick unit test notes:
    url test?
    view test?

    expected template?
    expected html?



TODO
YOU HAVE WRITTEN TOO MUCH CODE.
GO BACK TOMORROW TO THE ABOVE AND WRITE TESTS BEFORE YOU WRITE CODE!!!!