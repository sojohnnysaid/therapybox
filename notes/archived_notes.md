*******************************
*******
******* START 12/26/20
*******
*******************************


[✅] - TODO LIST
[✅] Create login page. This app does not have a traditional home page. The home page is either
the account page or the login page.
[✅] create a services folder with account_activation.py to skinny up UserRegisterView
and UserAccountActivationView

[✅] Tasks
[✅] Grab files, notes and todo.md needed and move to functional_tests/spikes
[✅] write out functional steps for account activation
[✅] write functional tests
[✅] write out unit steps for account activation



How account activation works:
    
    Functional
        1. user registers...
        2. user goes to email and clicks the link
        3. user is taken to login page showing the message "Your account has been activated! You can now login"

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


########shell scratchpad

from django.test import RequestFactory
from users import views
from django.urls import reverse, reverse_lazy
from django.contrib.auth import get_user_model
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode


email = 'johnsmith@gmail.com'
first_name = 'John'
password = 'p@assW0rd'

request = RequestFactory().post(reverse('users:users_register'), {
    'email': email,
    'first_name': first_name,
    'password1': password,
    'password2': password
})

view_instance = views.UsersRegisterView.as_view()
response = view_instance(request)

user = get_user_model().objects.get(email='johnsmith@gmail.com')
link = request.build_absolute_uri(reverse_lazy('users:users_account_activation'))
url_safe_user_pk = urlsafe_base64_decode(force_bytes(user.pk))
token = 


user.delete()

*******************************
*******
******* END 12/26/20
*******
*******************************

*******************************
*******
******* START 12/27/20
*******
*******************************

✅ TODO LIST 
[✅] explain from users perspective
[✅] explain from framework perspective
[✅] write unit tests
[✅] pass functional test


users perspective:
    goes to email...
    clicks the link
    is taken to the login page

framework perspective:
    url: 
        create patterns:
            ✅ users/account-activation/
            ✅ users/login/
    view:
        create views:
            ✅ UsersAccountActivationView
                responsibilities:
                    ✅ calling activate_user service with correct arguments
                    ✅ passing success message
                    ✅ redirecting to login page
            ✅ UsersLoginView
                responsibilities:
                    ✅ renders login page template
    service:
        create function:
            activate_user(request)
                responsibilities:
                    ✅ get relevant user from db using url query params
                    ✅ test if token is valid using user and url query params
                        Token is valid:
                            ✅ update user and save
                            ✅ return appropriate message
                        Token is invalid:
                            ✅ return appropriate message

*******************************
*******
******* END 12/27/20
*******
*******************************