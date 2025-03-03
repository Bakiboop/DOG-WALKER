from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()

class UserViewsTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Δημιουργία χρήστη για το login test
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpassword123',
            first_name='Test',
            last_name='User',
            phone_number='1234567890',
            address='Test Address'
        )

    def test_successful_login(self):
        response = self.client.post('/user/login/', {
            'email': 'test@example.com',
            'password': 'testpassword123'
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)  # Έλεγχος αν υπάρχει το token

    def test_invalid_login(self):
        response = self.client.post('/user/login/', {
            'email': 'test@example.com',
            'password': 'wrongpassword'
        })

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['error'], 'Invalid email or password.')

    def test_successful_signup(self):
        response = self.client.post('/user/signup/', {
            'first_name': 'New',
            'last_name': 'User',
            'email': 'newuser@example.com',
            'password': 'newpassword123',
            'phone_number': '0987654321',
            'address': 'New Address'
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Account successfully created')

        new_user = User.objects.filter(email='newuser@example.com').first()
        self.assertIsNotNone(new_user)

    def test_invalid_signup(self):
        response = self.client.post('/user/signup/', {
            'first_name': 'New',
            'last_name': 'User',
            'password': 'newpassword123',
            'phone_number': '0987654321',
            'address': 'New Address'
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)  # Πρέπει να υπάρχει error για το email
