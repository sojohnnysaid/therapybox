from django.db.models.expressions import OrderBy
from therapybox.models import TherapyBoxUser
from django.db import models

# Create your models here.

class Order(models.Model):
    class Meta:
        ordering = ['status']

    class Status(models.TextChoices):
        NEW = 1, 'New'
        LABELS_GENERATED = 2, 'Labels generated'
        SHIPPED = 3, 'Shipped'
        ARRIVED_AT_FACILITY = 4, 'Arrived at facility'
        CLOSED_ITEMS_RETURNED = 5, 'Closed items returned'

    class ShippingRegions(models.TextChoices):
        REGION_1 = 'REGION_1', 'Region 1'
        REGION_2 = 'REGION_2', 'Region 2'

    date_submitted = models.DateField(auto_now_add=True)
    product_id_list = models.CharField(max_length=40)
    user = models.ForeignKey(TherapyBoxUser, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=40, choices=Status.choices, blank=True, default=1)

    # billing
    billing_address_line_1 = models.CharField(max_length=128, blank=True)
    billing_address_line_2 = models.CharField(max_length=128, blank=True)
    billing_suburb = models.CharField(max_length=128, blank=True)
    billing_city = models.CharField(max_length=128, blank=True)
    billing_postcode = models.CharField(max_length=128, blank=True)
    
    # shipping
    shipping_address_line_1 = models.CharField(max_length=128, blank=True)
    shipping_address_line_2 = models.CharField(max_length=128, blank=True)
    shipping_suburb = models.CharField(max_length=128, blank=True)
    shipping_city = models.CharField(max_length=128, blank=True)
    shipping_postcode = models.CharField(max_length=128, blank=True)
    shipping_region = models.CharField(max_length=40, choices=ShippingRegions.choices, blank=True)

