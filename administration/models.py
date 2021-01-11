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

    date_submitted = models.DateField(auto_now_add=True)
    product_id_list = models.CharField(max_length=40)
    user = models.ForeignKey(TherapyBoxUser, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=40, choices=Status.choices, blank=True, default=1)

