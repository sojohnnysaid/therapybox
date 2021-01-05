import factory
from therapybox import models

class TherapyBoxTemplateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'therapybox.TherapyBoxTemplate'