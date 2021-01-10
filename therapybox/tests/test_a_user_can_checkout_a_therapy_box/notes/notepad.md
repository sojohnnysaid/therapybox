*******************************
*******
******* START xx/xx/xx
*******
*******************************

📜 Feature:
    ✅  A user can ...


✅ TODO LIST 
[] explain from users perspective
[] explain from framework perspective
[] write unit tests
[] pass functional test


users perspective:
    user logs in and sees library
    chooses and item
    user clicks add to cart on the details page
    user goes to another item and clicks add to cart
    user goes to cart page and chooses delivery date
    user sees shipping address
    user clicks checkout and sees confirmation page









from django.test import Client
from django.contrib.auth import get_user_model
user = get_user_model().objects.get(email='admin@gmail.com')
c = Client()
c.force_login(user)
from django.urls import reverse
res = c.get(reverse('administration:edit_therapy_box', args=[1]))
inspect(res)


framework perspective:

    [] service
        [] create methods:
            [] some_method(arg1)           
                [] responsibilities:
                    [] method is responsible for...

    [] form:
        [] responsibilities:
            [] form is responsible for...

    [] url name(name_of_url): 
        [] create patterns:
            [] my/url/pattern
        [] view class:
            [] ClassUrlCalls

    [] view MyViewName:
        [] responsibilities:
            [] form is responsible for...

    [] html templates
        [] create template:
            [] my_template_name.html
                [] responsibilities:


*******************************
*******
******* END xx/xx/xx
*******
*******************************