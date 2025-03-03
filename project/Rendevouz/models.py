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
    start_time=models.DateField()
    end_time=models.DateField(null=True)
    notes=models.TextField( null=True)
    dogs=models.PositiveSmallIntegerField()
    owner=models.ForeignKey(User,on_delete=models.CASCADE, related_name="appointment")
    type=models.CharField(max_length=2,choices=Appointment_types)
    
    
    def __str__(self):
        return f"{self.dogs.dog_name}'s appointment at {self.start_time}"

