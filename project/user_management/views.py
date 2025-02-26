from django.shortcuts import render, redirect
from user_management.forms import UserSignUp , UserLogin
from django.contrib.auth import login , authenticate
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSignUpSerializer
from .serializers import UserLoginSerializer
from .services import SignupService, LoginService


class signup_view(APIView):
    serializer_class=UserSignUpSerializer
    def __init__(self, signup_service: SignupService = None):
        self.signup_service = signup_service or SignupService()  # Εισαγωγή της υπηρεσίας

    def post(self, request, *args, **kwargs):
        # Χρήση του UserSignUpSerializer για επικύρωση των δεδομένων
        serializer = UserSignUpSerializer(data=request.data)
        
        if serializer.is_valid():
            # Χρήση της υπηρεσίας για την εγγραφή
            new_user = self.signup_service.signup(serializer.validated_data)
            
            # Αυθεντικοποίηση και σύνδεση του χρήστη
            email = serializer.validated_data.get('email')
            password = request.data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return Response({'message': 'Account successfully created'}, status=status.HTTP_201_CREATED)
            
            return Response({'error': 'Authentication failed'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Επιστροφή σφαλμάτων επικύρωσης
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class login_view(APIView):
    serializer_class=UserLoginSerializer
    def __init__(self, login_service: LoginService = None):
        self.login_service = login_service or LoginService()  # Εισαγωγή της υπηρεσίας

    def post(self, request, *args, **kwargs):
        # Χρήση του UserLoginSerializer για επικύρωση των δεδομένων
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Αν τα δεδομένα είναι έγκυρα, πάρτε τα επικυρωμένα δεδομένα
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        # Χρήση της υπηρεσίας για τη σύνδεση
        if self.login_service.login(request, email, password):
            return Response({'message': 'You have successfully logged in.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

def home(request):
    return render(request, 'home.html')







    


