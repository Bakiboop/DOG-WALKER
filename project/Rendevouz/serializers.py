from rest_framework import serializers
from .models import *

class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['breed', 'age', 'dog_name', 'owner']

class AppointmentBookingSerializer(serializers.ModelSerializer):
    dogs=serializers.PrimaryKeyRelatedField(queryset=Dog.objects.all())
    class Meta:
        model = Appointment_booking
        fields = [ 'start_time','end_time', 'notes', 'dogs','type']
        extra_kwargs = {
            'owner': {'read_only': True},  # Owner is automatically set to the current user
        }

