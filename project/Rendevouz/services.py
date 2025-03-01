from .models import Dog, Appointment_booking
from .serializers import DogSerializer, AppointmentBookingSerializer
from django.shortcuts import get_object_or_404

class DogService:
    def get_dog_by_id(self, user, pk):
        return get_object_or_404(Dog, owner=user, pk=pk)

    def get_dogs_by_owner(self, user):
        return Dog.objects.filter(owner=user)

    def create_dog(self, user, data):
        serializer = DogSerializer(data=data)
        if serializer.is_valid():
            serializer.save(owner=user)
            return serializer
        return None

    def update_dog(self, dog, data):
        serializer = DogSerializer(dog, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer
        return None

    def delete_dog(self, dog):
        dog.delete()

class AppointmentService:
    def get_appointment_by_id(self, user, pk):
        return get_object_or_404(Appointment_booking, owner=user, pk=pk)

    def get_appointments_by_owner(self, user):
        return Appointment_booking.objects.filter(owner=user)

    def create_appointment(self, user, data):
        serializer = AppointmentBookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save(owner=user)
            return serializer
        return None
    
    def update_appointment(self, appointment, data):
        serializer = AppointmentBookingSerializer(appointment, data=data)
        if serializer.is_valid():
            serializer.save()
            return serializer
        return None

    def delete_appointment(self, appointment):
        appointment.delete()