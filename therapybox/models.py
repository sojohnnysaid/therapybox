from django.db import models
from django.db.models.enums import Choices
from users.models import MyAbstractUser

# Create your models here.

class TherapyBoxUser(MyAbstractUser):

    class ShippingRegions(models.TextChoices):
        REGION_1 = 'REGION_1', 'Region 1'
        REGION_2 = 'REGION_2', 'Region 2'

    facility_name = models.CharField(max_length=128,)
    company_name = models.CharField(max_length=128,)
    phone_number = models.CharField(max_length=128,)
    point_of_contact = models.CharField(max_length=128,)
    address_line_1 = models.CharField(max_length=128,)
    address_line_2 = models.CharField(max_length=128,)
    suburb = models.CharField(max_length=128,)
    city = models.CharField(max_length=128,)
    postcode = models.CharField(max_length=128,)
    shipping_region = models.CharField(max_length=40, choices=ShippingRegions.choices)
    agreed_to_terms_and_conditions = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)