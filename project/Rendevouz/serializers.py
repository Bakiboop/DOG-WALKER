from rest_framework import serializers
from .models import *

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['id', 'breed', 'age', 'dog_name', 'owner']

class AppointmentBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment_booking
        fields = ['id', 'time', 'task', 'owner']