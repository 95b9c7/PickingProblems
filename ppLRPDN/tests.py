from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class MenuTest(TestCase):
    def setUp(self):
        # Create a test user and log them in
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_menu_protected(self):
        # Use the client to make a GET request to the menu URL
        response = self.client.get(reverse('menu'))

        # Check if the response status code is 200 (OK) for an authenticated user
        self.assertEqual(response.status_code, 200)

    def test_menu_not_protected(self):
        # Log the user out
        self.client.logout()

        # Use the client to make a GET request to the menu URL
        response = self.client.get(reverse('menu'))

        # Check if the response status code is 302 (Redirect) for an unauthenticated user
        self.assertEqual(response.status_code, 302)

        # Check if the user is redirected to the login page with the correct 'next' parameter
        self.assertRedirects(response, reverse('login') + '?next=' + reverse('menu'))