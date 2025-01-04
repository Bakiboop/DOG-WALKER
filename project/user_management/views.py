from django.shortcuts import render, redirect
from user_management.forms import UserSignUp , UserLogin
from django.contrib.auth import login , authenticate
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSignUpSerializer
from .serializers import UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class SignupView(APIView):
    serializer_class = UserSignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = UserSignUpSerializer(data=request.data)
        
        if serializer.is_valid():
            # Save the new user
            new_user = serializer.save()

            # Create JWT tokens
            refresh = RefreshToken.for_user(new_user)
            access_token = str(refresh.access_token)

            # Authenticate the user
            email = serializer.validated_data.get('email')
            password = request.data.get('password')  # Assuming password is passed in request
            
            authenticated_user = authenticate(request, email=email, password=password)
            if authenticated_user is not None:
                # Optional: Log the user in if you want them to be logged in immediately
                login(request, authenticated_user)
                messages.success(request, "Account successfully created")
                
                # You can return both JWT tokens and a success message
                return Response({
                    'message': 'Account successfully created',
                    'access': access_token,
                    'refresh': str(refresh),
                }, status=status.HTTP_201_CREATED)
            
            return Response({'error': 'Authentication failed'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Return validation errors if serializer is invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        # If you want to render a form-like response, you can optionally include this
        return Response({'message': 'Signup endpoint. Submit user data via POST.'})

class LoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        # Χρησιμοποιούμε τον UserLoginSerializer για επικύρωση των δεδομένων
        serializer = self.serializer_class(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Παίρνουμε τα επικυρωμένα δεδομένα
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        # Αυθεντικοποιούμε τον χρήστη
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            # Δημιουργούμε τα JWT tokens
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            
            # Επιλογή: Να κάνουμε login στο Django session ή να επιστρέψουμε JWT
            login(request, user)  # Αν θέλουμε να χρησιμοποιούμε Django session login
            messages.success(request, "You have successfully logged in.")
            
            # Επιστρέφουμε τα JWT tokens και το μήνυμα επιτυχίας
            return Response({
                'message': 'Login successful',
                'access': access_token,
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)

        # Επιστροφή σφάλματος αν τα credentials είναι λάθος
        return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request, *args, **kwargs):
        # Προαιρετική μέθοδος GET
        return Response({'message': 'Login endpoint. Submit email and password via POST.'})



def home(request):
    return render(request, 'home.html')



    


