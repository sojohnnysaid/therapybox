import factory
from therapybox import models
from django.contrib.auth.hashers import make_password

class TherapyBoxTemplateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'therapybox.TherapyBoxTemplate'


class TherapyBoxUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'therapybox.TherapyBoxUser'

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default ``_create`` with our custom call."""
        kwargs['password'] = make_password(kwargs['password'])
        return super(TherapyBoxUserFactory, cls)._create(model_class, *args, **kwargs)