from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    username = None 
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=50 )
    phone_number = models.CharField(max_length=10)
   

    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []  

    def __str__(self):
        return self.email


    