expected failure:
# John is taken to the login page
>       assert '/users/login/' in self.browser.current_url

[✅] Tasks

[✅] Grab files, notes and todo.md needed and move to functional_tests/spikes
[✅] write out functional steps for account activation
[✅] write functional tests
[ ] write out unit steps for account activation
[ ] write unit tests
[ ] see if functional test passes 100%


How account activation works:
    
    Functional
        1. user registers...
        2. user goes to email and clicks the link
        3. user is taken to login page showing the message "Your account has been activated! You can now login"

    Unit
        1. user registers...
            - post request to users_register 
            - UsersRegisterView form_valid method called: 
                - creates user
                - variables: link, url safe primary key, and token
                - insert variables into send_mail function
                - return super().form_valid(form)
                - success_url returns users_register_form_submitted template view

        2. user goes to email and clicks the link
            - get request to users_account_activation
            - UsersAccountActivationView get method called:
                - pull token, and url safe primary key from url query params
                - get the user using the primary key
                - if the token is not good guard and return error
                - otherwise set the user is_active to True
                - save the user
                - pass success message 'Your account has been activated! You can now login'
                - redirect to users_login page displaying success message