from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from user_management.models import User  # Import the custom User model
from .models import Appointment_booking
from .serializers import AppointmentBookingSerializer

class AppointmentsViewIntegrationTests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword123',
            address='123 Test St',
            phone_number='1234567890'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)  # Authenticate the user

        # Create a test appointment
        self.appointment = Appointment_booking.objects.create(
            start_time='2023-10-01T10:00:00Z',
            end_time='2023-11-01T12:00:00Z',
            notes='Regular checkup',
            dogs=1,
            owner=self.user,
            type='DW'  # Pet walking
        )

    def test_get_appointments(self):
        # Test listing all appointments for the authenticated user
        url = reverse('appointment')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one appointment exists
        self.assertEqual(response.data[0]['notes'], 'Regular checkup')

    def test_create_appointment(self):
        # Test creating a new appointment
        url = reverse('appointment')
        data = {
            'start_time': '2023-10-02T10:00:00Z',
            'end_time': '2023-10-02T12:00:00Z',
            'notes': 'New appointment',
            'dogs': 1,
            'type': 'PT'  # Pet taxi
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Appointment_booking.objects.count(), 2)  # Check if the appointment was created

    def test_update_appointment(self):
        # Test updating an existing appointment
        url = reverse('appointment')
        data = {
            'start_time': '2023-10-01T10:00:00Z',
            'end_time': '2023-11-01T13:00:00Z',  # Identify the appointment by start_time and type
            'type': 'DW',
            'notes': 'Updated notes',
            
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.appointment.refresh_from_db()  # Refresh the instance from the database
        self.assertEqual(self.appointment.notes, 'Updated notes')  # Check if the appointment was updated

    def test_delete_appointment(self):
        # Test deleting an existing appointment
        url = reverse('appointment')
        data = {
            'start_time': '2023-10-01T10:00:00Z',  # Identify the appointment by start_time and type
            'type': 'DW'
        }
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Appointment_booking.objects.count(), 0)  # Check if the appointment was deleted

    def test_create_appointment_invalid_data(self):
        # Test creating an appointment with invalid data
        url = reverse('appointment')
        data = {
            'start_time': '2023-10-02T10:00:00Z',
            'end_time': '2023-11-02T12:00:00Z',
            'notes': 'New appointment',
            'dogs': 1,
            # Missing 'type' field
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_appointment_not_found(self):
        # Test updating a non-existent appointment
        url = reverse('appointment')
        data = {
            'start_time': '2023-10-01T11:00:00Z',  # Incorrect start_time
            'type': 'DW',
            'notes': 'Updated notes',
            'end_time': '2023-10-01T13:00:00Z'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)  # Check if the error message is returned

    def test_delete_appointment_not_found(self):
        # Test deleting a non-existent appointment
        url = reverse('appointment')
        data = {
            'start_time': '2023-10-01T11:00:00Z',  # Incorrect start_time
            'type': 'DW'
        }
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('error', response.data)  # Check if the error message is returned