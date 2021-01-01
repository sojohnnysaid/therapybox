✅ TODO LIST 
[] register form action should be ""
[] remove is_active from managers.py
[] add from django.core.exceptions import ValidationError to admin.py
[] remove any imports no longer being used in forms, views etc.
[] add title template to shell template
#----------------------------------------------#
#                                              #
#----------------------------------------------#
[] update some tests that assert redirect to login view instead of home (assert 302 instead)
[] remove assert for users:login in UsersForgotPasswordResetViewTest
[] forms may need full_clean() before running save() UsersForgotPasswordResetView form_valid()
[] update UserCanActivateAccountUsingLinkOnceTest:
    # John is redirected to a new page
        new_page = str(conf_settings.LOGIN_REDIRECT_URL)
        assert new_page in self.browser.current_url



notes:
user is always is_authenticated
we need to add user to a group for permissions (this is for another feature)