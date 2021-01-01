




*******************************
*******
******* START 12/28/20
*******
*******************************

📜 Feature:
    ✅ A user can request to reset their password


✅ TODO LIST 
[✅] explain from users perspective
[✅] explain from framework perspective
[✅] write unit tests
[✅] pass functional test



users perspective:
    user goes to login page
    clicks forgot password link
    link takes them to password-reset-form page
    enters email
    submits form
    is redirected to login page with message 'password reset link sent to your email'


framework perspective:
    
    ✅ form:
        ✅ create form:
            ✅ email field
            ✅ use clean_email(self) method
                ✅ check if user exists. If not raise ValidationError('Email address not found in our system!')
    ✅ url name(password_reset_request): 
        ✅ create patterns:
            ✅ users/request-password-reset/

    ✅ view:
        ✅ create views:
            ✅ UsersForgotPasswordResetRequestView
                ✅ responsibilities:
                    ✅uses expected form class
                    ✅get method:
                        ✅returns expected html template
                    post method:
                        ✅calls send_password_reset_link service with expected arguments
                        ✅redirects to login page
                    
    ✅ service:
        ✅ create function signature:
            ✅ send_password_reset_link(request, user)
 
                    

*******************************
*******
******* END 12/29/20
*******
*******************************

*******************************
*******
******* START 12/29/20
*******
*******************************

📜 Feature:
    ✅  A user can reset password using emailed link once


✅ TODO LIST 
[✅] explain from users perspective
[✅] explain from framework perspective
[✅] write unit tests
[✅] pass functional test


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

    ✅ service
        ✅ create methods:
            ✅ get_password_reset_link(request, user)
                ✅ returns reset link including keywork arguments
            ✅ send_password_reset_link(request, user):
                ✅ responsibilities:
                    ✅ build send_email arguments
                    ✅ call send_email with correct arguments
                    ✅ return a success message
    ✅ form (uses form class in PasswordResetConfirmView):
    ✅ url name(password-reset): 
        ✅ create patterns:
            ✅ password-reset/<uidb64>/<token>/
        ✅ view class:
            ✅ UsersForgotPasswordResetView
    ✅ view UsersForgotPasswordResetView( inherits from PasswordResetConfirmView):
        ✅ important:
            ✅ declare INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'
            ✅ outside of class (see forgot_password_token_spike/views.py)
        ✅ overrides
            ✅ attributes:
                ✅ success_url = reverse_lazy('users:login')
                ✅ template_name = 'users/password_reset_form.html'
            ✅ methods:
                ✅ form_valid:
                    ✅ pass success message
    ✅ html templates
        ✅ create template:
            ✅ users_password_reset_form.html
                ✅ should include if else branches
                    ✅ form exists:
                        ✅ display the password reset form
                    ✅ form does not exist:
                        ✅ Display message token invalid
                        ✅ include link back to login page                   

*******************************
*******
******* END 12/30/20
*******
*******************************