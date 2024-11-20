from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonSignupSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer
from rest_framework.authtoken.models import Token
from .models import User
from django.contrib.auth.hashers import check_password
# Create your views here.

def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def home(request):
    return render(request, 'home.html')



class SignupView(generics.CreateAPIView):
    serializer_class = PersonSignupSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request):

        # Validate incoming data using the LoginSerializer
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            # Find user by email
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'error': 'user'}, status=status.HTTP_401_UNAUTHORIZED)
            
            # Check if the password matches
            if (user.password==password):
                # Password is correct, create or retrieve the token
                return Response({'token': 'uwu'}, status=status.HTTP_200_OK)
            else:
                # Password doesn't match
                return Response({'error': 'code'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


