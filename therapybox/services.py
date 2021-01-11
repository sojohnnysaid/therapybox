import datetime
import datedelta
from django.contrib import messages
from django.forms.widgets import DateInput

from therapybox.models import TherapyBox, TherapyBoxUser
from administration.models import Order

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
        user=user
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