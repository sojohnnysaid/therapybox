import factory
from factory import Faker
from django.contrib.auth.hashers import make_password
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.timezone import now


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'therapybox.Tag'

    name = Faker('name')
    


class TherapyBoxTemplateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'therapybox.TherapyBoxTemplate'

    name = Faker('name')
    image_1 = SimpleUploadedFile(name='test_image_1', content=open("static/test_uploads/test_image_1.png", 'rb').read(), content_type='image/png')

    tags = factory.RelatedFactoryList(
        TagFactory,
        size=4
    )


class TherapyBoxUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'therapybox.TherapyBoxUser'

    email = Faker('email')
    password = 'password'
    is_active = True
    facility_name = factory.Sequence(lambda n: "facility_%d" % n)


    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default ``_create`` with our custom call."""
        kwargs['password'] = make_password(kwargs['password'])
        return super(TherapyBoxUserFactory, cls)._create(model_class, *args, **kwargs)


class TherapyBoxFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'therapybox.TherapyBox'

    due_back = now()
    template = factory.SubFactory(TherapyBoxTemplateFactory)
