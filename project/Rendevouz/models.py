from django.db import models
from user_management.models import User







class Appointment_booking(models.Model):

    Appointment_types=[
        ('PW','pet walking'),
        ('PS','pet sitting'),
        ('PT', 'pet taxi'),]
    start_time=models.DateTimeField()
    end_time=models.DateTimeField(null=True)
    notes=models.TextField( null=True)
    dogs=models.PositiveSmallIntegerField()
    owner=models.ForeignKey(User,on_delete=models.CASCADE, related_name="appointment")
    type=models.CharField(max_length=2,choices=Appointment_types)
    
    
    def __str__(self):
        return f"{self.dogs.dog_name}'s appointment at {self.start_time}"

