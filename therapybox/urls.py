# users urls
from django.urls import path
from django.views.generic import TemplateView
from therapybox.views import *

app_name = 'therapybox'
urlpatterns = [
    path('', LibraryList.as_view(), name='list_library'),
    path('<int:pk>', LibraryDetail.as_view(), name='detail_library'),
    path('cart/', ShoppingCart.as_view(), name='shopping_cart'),
    path('add-to-cart/<int:pk>', AddToCart.as_view(), name='add_to_cart'),
    path('remove-from-cart/<int:pk>', RemoveFromCart.as_view(), name='remove_from_cart'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('paypal-instant-payment-notification/', PaypalInstantPaymentNotification.as_view(), name='paypal_instant_payment_notification'),
]