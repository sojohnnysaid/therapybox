*******************************
*******
******* START 12/29/20
*******
*******************************

📜 Feature:
    ✅  A user can reset password using emailed link once


✅ TODO LIST 
[] explain from users perspective
[] explain from framework perspective
[] write unit tests
[] pass functional test


users perspective:
    user checks email
    user sees a link and clicks it
    user is taken to a password reset form
    user enters password in password field
    user re-enters password in confirm field
    user submits the form
    user is taken to login page
    user sees message that password has been reset


framework perspective:
    ✅ form (uses form class in PasswordResetConfirmView):
    url name(forgot_password_reset_form): 
        create patterns:
            forgot-password-reset-form/<uidb64>/<token>/
        calls:
            UsersPasswordResetView.as_view()
    view UsersPasswordResetView( inherits from PasswordResetConfirmView):
        important:
            declare INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'
            outside of class (see forgot_password_token_spike/views.py)
        overrides
            attributes:
                success_url = reverse_lazy('users:login')
                template_name = 'users/users_password_reset_form.html'
            methods:
                form_valid:
                    pass success message
    ✅ service (no services in this feature)
    html templates
        create template:
            users_password_reset_form.html
                should include if else branches
                    form exists:
                        display the password reset form
                    form does not exist:
                        Display message token invalid
                        include link back to login page

    
            
 
                    

*******************************
*******
******* END 12//20
*******
*******************************