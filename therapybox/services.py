import datetime
import datedelta
import os
from django.contrib import messages
from django.forms.widgets import DateInput
from django.http.response import HttpResponseRedirect

from therapybox.models import TherapyBox, TherapyBoxUser
from administration.models import Order

from paypalrestsdk import Payment

from dotenv import load_dotenv
load_dotenv()

# def get_min_calendar_date(): # this function will get you the closest Tuesday to ship something out
#     today = datetime.date.today()

#     # today = today + datedelta.datedelta(days=+2) # test with other days

#     tuesday = 1 # days are numbered Monday=0 Sunday=6
#     min = today + datetime.timedelta(days=(tuesday - today.weekday() + 7 ) %7 )

#     if today.weekday() == tuesday:
#         # add another week of lead time
#         min = today + datetime.timedelta(days=(tuesday - today.weekday() + 7 ) %7 + 7)

#     return min


# def get_max_calendar_date():
#     return datetime.date.today() + datedelta.datedelta(months=2)


# def get_custom_date_input():
#     return DateInput(attrs={'type': 'date', 'min': get_min_calendar_date(), 'max': get_max_calendar_date(), 'step': '7'})


def create_new_order(request):
    # get the dictionary of item ids
    items = request.session['cart']['items']

    # get the query set
    queryset = TherapyBox.objects.filter(pk__in=items)

    # get the user
    user = TherapyBoxUser.objects.get(email=request.user.email)

    if not all([item.status == 'AVAILABLE' for item in queryset]):
        new_items = list(filter(lambda item: item.status == 'AVAILABLE', queryset))
        new_items = [item.id for item in new_items]
        request.session['cart']['items'] = new_items
        request.session.save()
        return messages.error(
            request, 
            'An item in your cart was requested before this order was processed. We\'ve removed the item from your cart. Please try again.')

    
    # create order
    product_id_list = ','.join(map(str, items))
    Order.objects.create(
        product_id_list=product_id_list,
        user=user,
        billing_address_line_1 = user.billing_address_line_1,
        billing_address_line_2 = user.billing_address_line_2,
        billing_suburb = user.billing_suburb,
        billing_city = user.billing_city,
        billing_postcode = user.billing_postcode,
        shipping_address_line_1 = user.shipping_address_line_1,
        shipping_address_line_2 = user.shipping_address_line_2,
        shipping_suburb = user.shipping_suburb,
        shipping_city = user.shipping_city,
        shipping_postcode = user.shipping_postcode,
        shipping_region = user.shipping_region
    )

    #empty the cart
    request.session['cart']['items'] = []
    request.session.save()

    #update all items to borrowed
    queryset.update(status='BORROWED')

    #add success message
    return messages.success(
            request, 
            f'Thank you for your order! Your receipt will be emailed to {request.user.email}.')



def create_payment(request):
    from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


    # Creating Access Token for Sandbox
    client_id = os.getenv("PAYPAL_CLIENT_ID")
    client_secret = os.getenv("PAYPAL_SECRET_ID")
    # Creating an environment
    environment = SandboxEnvironment(client_id=client_id, client_secret=client_secret)
    client = PayPalHttpClient(environment)

    from paypalcheckoutsdk.orders import OrdersCreateRequest
    from paypalhttp import HttpError
    # Construct a request object and set desired parameters
    # Here, OrdersCreateRequest() creates a POST request to /v2/checkout/orders
    request = OrdersCreateRequest()

    request.prefer('return=representation')

    request.request_body (
        {
            "intent": "CAPTURE",
            "purchase_units": [
                {
                    "amount": {
                        "currency_code": "USD",
                        "value": "100.00"
                    }
                }
            ]
        }
    )

    try:
        # Call API with your client and get a response for your call
        response = client.execute(request)
        print('Order With Complete Payload:')
        print('Status Code:', response.status_code)
        print('Status:', response.result.status)
        print('Order ID:', response.result.id)
        print('Intent:', response.result.intent)
        print('Links:')
        for link in response.result.links:
            print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
            print('Total Amount: {} {}').format(response.result.purchase_units[0].amount.currency_code,
            response.result.purchase_units[0].amount.value)
            # If call returns body in response, you can get the deserialized version from the result attribute of the response
            order = response.result
            print(order)
    except IOError as ioe:
        print(ioe)
        if isinstance(ioe, HttpError):
            # Something went wrong server-side
            print(ioe.status_code)