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