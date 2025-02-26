from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from rest_framework import status
from .views import login_view, signup_view
from .serializers import UserLoginSerializer, UserSignUpSerializer

User = get_user_model()

class UserViewsTest(TestCase):
    def setUp(self):
        # Δημιουργία ενός χρήστη για testing
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpassword123',
            first_name='Test',
            last_name='User',
            phone_number='1234567890',
            address='Test Address'
        )
        self.factory = RequestFactory()

    # Tests για το login_view
    def test_successful_login(self):
        # Δημιουργία ενός POST request με έγκυρα δεδομένα
        request = self.factory.post('/login/', {
            'email': 'test@example.com',
            'password': 'testpassword123'
        })
        response = login_view().post(request)
        
        # Έλεγχος αν η απάντηση είναι επιτυχής
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'You have successfully logged in.')

    def test_invalid_login(self):
        # Δημιουργία ενός POST request με λάθος κωδικό
        request = self.factory.post('/login/', {
            'email': 'test@example.com',
            'password': 'wrongpassword'
        })
        response = login_view().post(request)
        
        # Έλεγχος αν η απάντηση είναι 401 Unauthorized
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['error'], 'Invalid email or password.')

    # Tests για το signup_view
    def test_successful_signup(self):
        # Δημιουργία ενός POST request με έγκυρα δεδομένα
        request = self.factory.post('/signup/', {
            'first_name': 'New',
            'last_name': 'User',
            'email': 'newuser@example.com',
            'password': 'newpassword123',
            'phone_number': '0987654321',
            'address': 'New Address'
        })
        response = signup_view().post(request)
        
        # Έλεγχος αν η απάντηση είναι επιτυχής
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Account successfully created')

        # Έλεγχος αν ο νέος χρήστης δημιουργήθηκε στη βάση δεδομένων
        new_user = User.objects.filter(email='newuser@example.com').first()
        self.assertIsNotNone(new_user)

    def test_invalid_signup(self):
        # Δημιουργία ενός POST request με λάθος δεδομένα (λείπει το email)
        request = self.factory.post('/signup/', {
            'first_name': 'New',
            'last_name': 'User',
            'password': 'newpassword123',
            'phone_number': '0987654321',
            'address': 'New Address'
        })
        response = signup_view().post(request)
        
        # Έλεγχος αν η απάντηση είναι 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)  # Έλεγχος αν το σφάλμα αναφέρει το email
