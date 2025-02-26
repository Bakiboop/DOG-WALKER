from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import make_password
from user_management.models import User

class SignupService:
    def signup(self, data):
        # Λογική για την εγγραφή χρήστη
        password = data.get('password')
        hashed_password = make_password(password)
        user = User.objects.create(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            password=hashed_password,
            phone_number=data.get('phone_number'),
            address=data.get('address')
        )
        return user

class LoginService:
    def login(self, request, email, password):
        # Λογική για τη σύνδεση χρήστη
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return True
        return False