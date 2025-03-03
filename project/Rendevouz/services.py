from .models import Appointment_booking
from .serializers import AppointmentBookingSerializer
from django.core.exceptions import ValidationError

class AppointmentService:
    def get_appointments_by_owner(self, user):
        # Retrieve all appointments for the given user
        return Appointment_booking.objects.filter(owner=user)

    def create_appointment(self, user, data):
        # Create a new appointment for the user
        serializer = AppointmentBookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save(owner=user)
            return serializer
        raise ValidationError(serializer.errors)

    def update_appointment(self, user, data):
        # Update an existing appointment based on unique fields (e.g., start_time and type)
        start_time = data.get('start_time')
        appointment_type = data.get('type')

        if not start_time or not appointment_type:
            raise ValidationError("Both 'start_time' and 'type' are required to identify the appointment.")

        # Find the appointment by start_time and type
        appointment = Appointment_booking.objects.filter(
            owner=user,
            start_time=start_time,
            type=appointment_type
        ).first()

        if not appointment:
            raise ValidationError("Appointment not found.")

        # Update the appointment
        serializer = AppointmentBookingSerializer(appointment, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return serializer
        raise ValidationError(serializer.errors)

    def delete_appointment(self, user, data):
        # Delete an existing appointment based on unique fields (e.g., start_time and type)
        start_time = data.get('start_time')
        appointment_type = data.get('type')

        if not start_time or not appointment_type:
            raise ValidationError("Both 'start_time' and 'type' are required to identify the appointment.")

        # Find the appointment by start_time and type
        appointment = Appointment_booking.objects.filter(
            owner=user,
            start_time=start_time,
            type=appointment_type
        ).first()

        if not appointment:
            raise ValidationError("Appointment not found.")

        # Delete the appointment
        appointment.delete()