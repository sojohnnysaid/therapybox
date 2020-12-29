*******************************
*******
******* START 12/28/20
*******
*******************************

📜 Feature:
    A user can request to reset their password


✅ TODO LIST 
[✅] explain from users perspective
[✅] explain from framework perspective
[] write unit tests
[] pass functional test


user story:
    user can request password reset


users perspective:
    user goes to login page
    clicks forgot password link
    link takes them to password-reset-form page
    enters email
    submits form
    is redirected to login page with message 'password reset link sent to your email'


framework perspective:
    ✅ url: 
        ✅ create patterns:
            ✅ users/request-password-reset/
            users/password-reset/
    form:
        create form:
            X email field
            X use clean_email(self) method
                X check if user exists. If not raise ValidationError('Email address not found in our system!')
    view:
        create views:
            UsersPasswordResetRequestView
                responsibilities:
                    handles request in form_valid method
                        get the user object based on form.cleaned_data['email']
                        calls send_password_reset_link service with expected arguments
                        redirects to login page
                    
    service:
        create functions:
            get_password_reset_link(request, user)
                responsibilities:
                    build link from token, uid, and absolute_uri
                    return link
            send_password_reset_link(request)
                responsibilities:
                    build send email
                        email_subject
                        email_body using get_password_reset_link
                        email_from
                        email_to
                    return send_mail with expected arguments
 
                    

*******************************
*******
******* END 12/28/20
*******
*******************************



#djshell scratch pad notes
from django.contrib.auth import get_user_model
from random import randrange
from django.contrib.auth.tokens import default_token_generator
from django.test import Client

# create a user
email = f'{randrange(100000)}test_password_reset@gmail.com'
password = 'pPa@ssw0rd'
user = get_user_model().objects.create_user(email=email, password=password)

# generate a password reset token
token = default_token_generator.make_token(user)

# check if token is valid
default_token_generator.check_token(user, token)
default_token_generator.check_token(user, token)
default_token_generator.check_token(user, token)
default_token_generator.check_token(user, token)

# login the user
client = Client()
client.force_login(user)

# check if token is still valid
default_token_generator.check_token(user, token)
default_token_generator.check_token(user, token)
default_token_generator.check_token(user, token)
default_token_generator.check_token(user, token)







from django.test import RequestFactory
from django.urls import reverse
from users import views

request = RequestFactory().get(reverse('users:password_reset_request'))
response = views.UsersPasswordResetRequestView.as_view()(request)
response.template_name[0]





from django.contrib.auth import get_user_model

user = get_user_model().objects.get(email='nope@aol.com')