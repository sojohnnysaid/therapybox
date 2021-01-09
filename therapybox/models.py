from django.db import models
from django.db.models.enums import Choices
from django.urls import reverse


from users.models import MyAbstractUser

from cloudinary.models import CloudinaryField


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




class Tag(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name




class TherapyBoxTemplate(models.Model):
    class Meta:
        ordering = ['-id']

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128, blank=True)
    tags = models.ManyToManyField(Tag)
    image_1 = CloudinaryField('Image 1', blank=True)
    image_2 = CloudinaryField('Image 2', blank=True)
    image_3 = CloudinaryField('Image 3', blank=True)
    tags = models.CharField(max_length=128, blank=True)
    length = models.CharField(max_length=128, help_text='Approx mm', blank=True)
    height = models.CharField(max_length=128, help_text='Approx mm', blank=True)
    depth = models.CharField(max_length=128, help_text='Approx mm', blank=True)
    weight = models.CharField(max_length=128, help_text='Approx kg', blank=True)




    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('administration:catalog')


class TherapyBox(models.Model):
    class Locations(models.TextChoices):
        STORAGE = 'STORAGE', 'Storage'

    class Status(models.TextChoices):
        AVAILABLE = 'AVAILABLE', 'Available'
        BLOCKED = 'REGION_2', 'Region 2'

    class Condition(models.TextChoices):
        GOOD = 'GOOD', 'Good'
        BROKEN = 'BROKEN', 'Broken'
        MISSING = 'MISSING', 'Missing'
        UNDER_DEVELOPMENT = 'UNDER_DEVELOPMENT', 'Under development'
        WAITING_FOR_PART = 'WAITING_FOR_PART', 'Waiting for a part'

    template = models.ForeignKey('TherapyBoxTemplate', on_delete=models.RESTRICT)
    location = models.CharField(max_length=40, choices=Locations.choices, blank=True)
    status = models.CharField(max_length=40, choices=Status.choices, blank=True)
    condition = models.CharField(max_length=40, choices=Condition.choices, blank=True)
    due_back = models.DateField(null=True, blank=True)
    notes = models.TextField()

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        string_id = str(self.id)
        return f"{string_id.rjust(3,'0')} {self.template.name}"

    def get_absolute_url(self):
        return reverse('administration:inventory')
