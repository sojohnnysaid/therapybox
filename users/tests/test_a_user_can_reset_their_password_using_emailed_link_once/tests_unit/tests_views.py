from django.test.testcases import TestCase
from django.urls import reverse
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model

from django.test import Client
from django.conf import settings as conf_settings

from users import services





class BaseTestCase(TestCase):

    def setUp(self):
        super().setUp()
        email = 'john@gmail.com'
        password = 'pP@assW0rd'
        self.user = get_user_model().objects.create_user(email=email, password=password)




class UsersPasswordResetViewTest(BaseTestCase):

    def test_success_url_goes_to_expected_path_on_successful_password_reset(self):        
        request = RequestFactory().get('') # request path not important in this case

        url = services.get_password_reset_link(request, self.user)
        uidb64 = url.split('/')[5]
        token = url.split('/')[6]

        new_password = 'AuniqueNewPW2rrrd$'
        c = Client()
        response = c.get(
            reverse('users:password-reset', kwargs={'uidb64': uidb64, 'token': token}), follow=True)
        
        self.assertTemplateUsed(response, 'users/password_reset_form.html')
        
        response = c.post(
            reverse('users:password-reset', kwargs={'uidb64': uidb64, 'token': 'set-password'}),
            {'new_password1': new_password, 'new_password2': new_password}, follow=True)

        self.assertContains(response, 'Success! Your password has been reset.')
        self.assertEqual(response.url, conf_settings.USERS_PASSWORD_RESET_FORM_SUCCESS_URL)
        

    def test_new_password_is_valid(self):
        request = RequestFactory().get('') # request path not important in this case

        url = services.get_password_reset_link(request, self.user)
        uidb64 = url.split('/')[5]
        token = url.split('/')[6]

        UserModel = get_user_model()
        new_password = UserModel.objects.make_random_password()

        c = Client()
        c.get(
            reverse('users:password-reset', kwargs={'uidb64': uidb64, 'token': token}), follow=True)
        c.post(
            reverse('users:password-reset', kwargs={'uidb64': uidb64, 'token': 'set-password'}),
            {'new_password1': new_password, 'new_password2': new_password}, follow=True)

        
        fresh_user = UserModel.objects.get(email=self.user.email)
        self.assertTrue(fresh_user.check_password(new_password))