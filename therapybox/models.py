from django.db import models
from django.db.models.enums import Choices
from users.models import MyAbstractUser

# Create your models here.

class TherapyBoxUser(MyAbstractUser):

    REQUIRED_FIELDS = []

    class ShippingRegions(models.TextChoices):
        REGION_1 = 'REGION_1', 'Region 1'
        REGION_2 = 'REGION_2', 'Region 2'

    facility_name = models.CharField(max_length=128, blank=True)
    company_name = models.CharField(max_length=128, blank=True)
    phone_number = models.CharField(max_length=128, blank=True)
    point_of_contact = models.CharField(max_length=128, blank=True)
    address_line_1 = models.CharField(max_length=128, blank=True)
    address_line_2 = models.CharField(max_length=128, blank=True)
    suburb = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=128, blank=True)
    postcode = models.CharField(max_length=128, blank=True)
    shipping_region = models.CharField(max_length=40, choices=ShippingRegions.choices, blank=True)
    agreed_to_terms_and_conditions = models.BooleanField(default=False, blank=True)
    is_approved = models.BooleanField(default=False, blank=True)