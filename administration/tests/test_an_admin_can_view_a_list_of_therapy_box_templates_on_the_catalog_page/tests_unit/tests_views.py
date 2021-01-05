from unittest import skip
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from factories.factories import TherapyBoxTemplateFactory




class BaseTestCase(TestCase):

    def setUp(self):
        super().setUp()
        self.User = get_user_model()
        self.email = 'test@gmail.com'
        self.password = 'password'
        self.client = Client()

    def login_user(self):
        user = self.User.objects.create(email=self.email, password=self.password)
        self.client.force_login(user)
    
    def login_admin(self):
        user = self.User.objects.create(email=self.email, password=self.password)
        user.is_admin = True
        user.is_active = True
        user.save()
        self.client.force_login(user)


class ViewTest(BaseTestCase):


    def test_catalog_page_shows_list_of_therapy_box_templates(self):
        TherapyBoxTemplateFactory(name='a new therapy box template')
        TherapyBoxTemplateFactory(name='another therapy box template')
        self.login_admin()
        response = self.client.get(reverse('administration:catalog'), follow=True)
        assert 'a new therapy box template' in response.rendered_content
        assert 'another therapy box template' in response.rendered_content