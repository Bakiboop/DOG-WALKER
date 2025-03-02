from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from user_management.models import User  # Import the custom User model
from .models import Dog, Appointment_booking
from .serializers import DogSerializer, AppointmentBookingSerializer

class DogViewIntegrationTests(APITestCase):
    def setUp(self):
        # Create a test user using the custom User model
        self.user = User.objects.create_user(
            username='testuser@example.com',
            email='testuser@example.com',
            password='testpassword123',
            address='123 Test St',
            phone_number='1234567890'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)  # Authenticate the user

        # Create a test dog
        self.dog = Dog.objects.create(
            breed='Labrador',
            age=3,
            dog_name='Buddy',
            owner=self.user
        )

    def test_create_dog(self):
        url = reverse('dog-list')  # Assuming you have named your URL pattern
        data = {
            'breed': 'Golden Retriever',
            'age': 2,
            'dog_name': 'Max'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Dog.objects.count(), 2)  # Check if the dog was created

    def test_get_dog(self):
        url = reverse('dog-detail', args=[self.dog.id])  # URL for the specific dog
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['dog_name'], 'Buddy')  # Check if the correct dog is returned

    def test_update_dog(self):
        url = reverse('dog-detail', args=[self.dog.id])
        data = {
            'breed': 'Labrador',
            'age': 4,
            'dog_name': 'Buddy Updated'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.dog.refresh_from_db()  # Refresh the instance from the database
        self.assertEqual(self.dog.dog_name, 'Buddy Updated')  # Check if the dog was updated

    def test_delete_dog(self):
        url = reverse('dog-detail', args=[self.dog.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Dog.objects.count(), 0)  # Check if the dog was deleted

class AppointmentsViewIntegrationTests(APITestCase):
    def setUp(self):
        # Create a test user using the custom User model
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword123',
            address='123 Test St',
            phone_number='1234567890'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)  # Authenticate the user

        # Create a test dog
        self.dog = Dog.objects.create(
            breed='Labrador',
            age=3,
            dog_name='Buddy',
            owner=self.user
        )


        # Create a test appointment
        self.appointment = Appointment_booking.objects.create(
            start_time='2023-10-01T10:00:00Z',
            end_time='2023-10-01T12:00:00Z',
            notes='Regular checkup',
            dogs=self.dog,
            owner=self.user,
            type='PW'  # Pet walking
        )

    def test_create_appointment(self):
        url = reverse('appointments-list')  # Assuming you have named your URL pattern
        data = {
            'start_time': '2023-10-02T10:00:00Z',
            'end_time': '2023-10-02T12:00:00Z',
            'notes': 'New appointment',
            'dogs': self.dog.id,  # Primary key of the dog
            'type': 'PS'  # Pet sitting
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Appointment_booking.objects.count(), 2)  # Check if the appointment was created

    def test_get_appointment(self):
        url = reverse('appointments-detail', args=[self.appointment.id])  # URL for the specific appointment
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['notes'], 'Regular checkup')  # Check if the correct appointment is returned

    def test_update_appointment(self):
        url = reverse('appointments-detail', args=[self.appointment.id])
        data = {
            'start_time': '2023-10-01T11:00:00Z',
            'end_time': '2023-10-01T13:00:00Z',
            'notes': 'Updated notes',
            'dogs': self.dog.id,
            'type': 'PT'  # Pet taxi
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.appointment.refresh_from_db()  # Refresh the instance from the database
        self.assertEqual(self.appointment.notes, 'Updated notes')  # Check if the appointment was updated

    def test_delete_appointment(self):
        url = reverse('appointments-detail', args=[self.appointment.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Appointment_booking.objects.count(), 0)  # Check if the appointment was deleted