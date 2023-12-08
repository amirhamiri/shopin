from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User
from django.contrib.messages import get_messages

class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('accounts:login')
        self.user = User.objects.create_user(phone='11234567890', password='testpassword123')
        self.user.save()

    def test_login_page_GET(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login_form.html')

    def test_login_POST_with_correct_credentials(self):
        response = self.client.post(self.login_url, {'phone': '11234567890', 'password': 'testpassword123'})
        self.assertRedirects(response, reverse('accounts:login'))

    def test_login_POST_with_incorrect_credentials(self):
        response = self.client.post(self.login_url, {'phone': '11234567890', 'password': 'wrongpassword'})
        self.assertRedirects(response, self.login_url)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Invalid phone or password.")

    def test_login_POST_with_inactive_user(self):
        self.user.is_active = False
        self.user.save()
        response = self.client.post(self.login_url, {'phone': '11234567890', 'password': 'testpassword123'})
        self.assertRedirects(response, self.login_url)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Invalid phone or password.")
