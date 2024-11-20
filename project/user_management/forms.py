from django import forms
from django.contrib.auth.forms import UserCreationForm ,  AuthenticationForm
from user_management.models import User


class UserSignUp(UserCreationForm):
    
    class Meta:
        model = User 
        fields = ['first_name' , 'last_name' , 'email' , 'phone_number' , 'address']



class UserLogin(UserCreationForm):
     class Meta:
       model = User
       fields = ['email' , 'password']
        
        