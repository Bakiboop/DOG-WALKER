from django.db import models
from user_management.models import User

class Dog(models.Model):
    breed=models.CharField(max_length=30)
    age=models.SmallIntegerField()
    dog_name=models.TextField()
    owner=models.ForeignKey(User , on_delete=models.CASCADE)





class Appointment_booking(models.Model):
    time=models.DateTimeField()
    avaiable_tasks = [
    ("WK" , "Walk"),
    ("PT" , "Pet taxi"),
    ("PS" , "Pet sitting"),
]
    task=models.CharField(max_length=2,choices=avaiable_tasks)
    owner =models.ForeignKey(User , on_delete=models.CASCADE)
    

