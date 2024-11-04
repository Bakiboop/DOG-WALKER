from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128) 
    
class Person(User):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    address = models.CharField(max_length= 50)
    phone_number = models.IntegerField()
    
    
  
    
