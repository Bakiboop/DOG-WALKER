from rest_framework import serializers
from .models import *



class AppointmentBookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Appointment_booking
        fields = [ 'start_time','end_time', 'notes', 'dogs','type']
        extra_kwargs = {
            'owner': {'read_only': True},  # Owner is automatically set to the current user
        }

