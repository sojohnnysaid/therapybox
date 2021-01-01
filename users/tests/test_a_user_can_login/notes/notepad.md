*******************************
*******
******* START xx/xx/xx
*******
*******************************

📜 Feature:
    ✅  A user can login


✅ TODO LIST 
[] explain from users perspective
[] explain from framework perspective
[] write unit tests
[] pass functional test


users perspective:
    user goes to the login page
    user enters username
    user enters password
    user clicks submit
    user is taken to homepage
    there is a message on the homepage letting them know they are successfully logged in



framework perspective:

    [✅] url name(name_of_url): 
        [] create patterns:
            [] login/
        [] view class:
            [] UsersLoginView

    [] view UsersLoginView(inherts mostly from LoginView):
        [] responsibilities:
            [] declare template_name = 'users/login.html'
            [] success_url = '/'
            [] display the template to the user

    [] form we are using the framework implementation:
        [] responsibilities:
            [] We only need to include {form} in the template

    [] html templates
        [] create template:
            [] login.html
                [] responsibilities:
                    [] display form
                    [] display messages


*******************************
*******
******* END xx/xx/xx
*******
*******************************