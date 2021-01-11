A user can submit an order

    user clicks checkout
    col1
    checkout page shows billings, shipping
    col2
    items listed

    Order Date: today
    Due date: 2 months from today

    Borrow Items


paypal:
    https://developer.paypal.com/docs/api/quickstart/payments/
    small window
    <a href="yourpage.htm" target="_blank" onClick="window.open('https://www.google.com','pagename','resizable,height=600,width=800,top=150,left=400'); return false;">New Page</a>


from administration.models import Order
all = Order.objects.all()
x = all[4]
inspect(x)