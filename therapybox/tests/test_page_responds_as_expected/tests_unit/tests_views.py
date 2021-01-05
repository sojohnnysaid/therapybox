from unittest import skip
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model




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
        user.save()
        self.client.force_login(user)


class ViewTest(BaseTestCase):

    # public routes

    def test_homepage_returns_page_status_ok(self):
        url_name = 'debug'
        response = self.client.get(reverse(url_name))
        self.assertEqual(response.status_code, 200)

    def test_register_returns_page_status_ok(self):
        url_name = 'users:register'
        response = self.client.get(reverse(url_name))
        self.assertEqual(response.status_code, 200)

    def test_account_activation_request_returns_page_status_ok(self):
        url_name = 'users:account_activation_request'
        response = self.client.get(reverse(url_name))
        self.assertEqual(response.status_code, 200)

    def test_password_request_reset_link_returns_page_status_ok(self):
        url_name = 'users:password_request_reset_link'
        response = self.client.get(reverse(url_name))
        self.assertEqual(response.status_code, 200)

    def test_user_login_returns_page_status_ok(self):
        url_name = 'users:login'
        response = self.client.get(reverse(url_name))
        self.assertEqual(response.status_code, 200)
    
    def test_admin_login_returns_page_status_ok(self):
        url_name = 'users:admin_login'
        response = self.client.get(reverse(url_name))
        self.assertEqual(response.status_code, 200)




    # administration routes

    def test_django_admin_redirects_to_login(self):
        django_admin_url = '/control-panel/'
        response = self.client.get(django_admin_url)
        self.assertRedirects(response, '/control-panel/login/?next=/control-panel/')


    def test_admin_only_url_returns_redirect_to_admin_login(self):
        url_name = 'administration:admin_base'
        response = self.client.get(reverse(url_name), follow=True)
        self.assertRedirects(response, reverse('users:admin_login'))
    

    def test_dashboard_redirects_to_admin_login_when_not_logged_in(self):
        url_name = 'administration:dashboard'
        response = self.client.get(reverse(url_name), follow=True)
        self.assertRedirects(response, reverse('users:admin_login'))
    

    def test_dashboard_redirects_to_admin_login_when_user_not_admin_logged_in(self):
        self.login_user()
        url_name = 'administration:dashboard'
        response = self.client.get(reverse(url_name), follow=True)
        self.assertRedirects(response, reverse('users:admin_login'))


    def test_catalog_redirects_to_admin_login_when_not_logged_in(self):
        url_name = 'administration:catalog'
        response = self.client.get(reverse(url_name), follow=True)
        self.assertRedirects(response, reverse('users:admin_login'))

    
    def test_catalog_redirects_to_admin_login_when_user_not_admin_logged_in(self):
        self.login_user()
        url_name = 'administration:catalog'
        response = self.client.get(reverse(url_name), follow=True)
        self.assertRedirects(response, reverse('users:admin_login'))

    
    def test_create_therapy_box_template_redirects_to_admin_login_when_not_logged_in(self):
        url_name = 'administration:create_therapy_box_template'
        response = self.client.get(reverse(url_name), follow=True)
        self.assertRedirects(response, reverse('users:admin_login'))
    

    def test_create_therapy_box_template_redirects_to_admin_login_when_user_not_admin_logged_in(self):
        self.login_user()
        url_name = 'administration:create_therapy_box_template'
        response = self.client.get(reverse(url_name), follow=True)
        self.assertRedirects(response, reverse('users:admin_login'))

    
    