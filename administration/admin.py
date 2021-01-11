from django.contrib import admin
from therapybox import models
from administration.models import Order
# Register your models here.

admin.site.register(models.TherapyBoxTemplate)
admin.site.register(models.TherapyBox)
admin.site.register(Order)