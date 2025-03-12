from django.db import models
from user_management.models import User







class Appointment_booking(models.Model):

    Appointment_types=[
        ('DG', 'Dog Walking'),
        ('PM','Pet Sitting My Home'),
        ('PY','Pet Sitting Your Home'),
        ('PT', 'Pet Taxi'),
        ('AL', 'Other')
        ]
    start_time=models.DateTimeField()
    end_time=models.DateTimeField(null=True)
    notes=models.TextField( null=True)
    dogs=models.PositiveSmallIntegerField()
    owner=models.ForeignKey(User,on_delete=models.CASCADE, related_name="appointment")
    type=models.CharField(max_length=2,choices=Appointment_types)


    
 