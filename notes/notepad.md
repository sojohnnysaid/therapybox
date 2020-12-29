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
    
     form:
        create form:
            UsersPasswordResetForm
                fields:
                    new_password1
                    new_password2
                responsibilities:
                    verifies password fields match
                    verifies password is valid
                    updates user's password in database
                    returns user object
     url name(forgot_password_reset_form): 
         create patterns:

             
     view:
         create views:
            
     service:
         function:
            
 
                    

*******************************
*******
******* END 12//20
*******
*******************************