✅ TODO LIST 
[] explain from users perspective
[] explain from framework perspective
[] write unit tests
[] pass functional test


functional test:
    current expected failure:
        self.user_submits_reset_password_form('John') # mail.outbox[0] will hold account activation email
        # John goes to his email...
>       email = mail.outbox[1]
E       IndexError: list index out of range


    quick unit test notes:
        url path?
        view?
        service?