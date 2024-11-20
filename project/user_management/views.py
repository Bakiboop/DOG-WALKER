from django.shortcuts import render, redirect
from user_management.forms import UserSignUp , UserLogin
from django.contrib.auth import login , authenticate
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSignUpSerializer
from .serializers import UserLoginSerializer


class signup_view(APIView):
    serializer_class =  UserSignUpSerializer
    def post(self, request, *args, **kwargs):
        serializer = UserSignUpSerializer(data=request.data)
        
        if serializer.is_valid():
            # Save the new user
            new_user = serializer.save()
            
            # Authenticate the user
            email = serializer.validated_data.get('email')
            password = request.data.get('password')  # Assuming password is passed in request
            
            new_user = authenticate(request, email=email, password=password)
            if new_user is not None:
                login(request, new_user)
                messages.success(request, "Account successfully created")
                return redirect("login")
            
            return Response({'error': 'Authentication failed'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Return validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        # If you want to render a form-like response, you can optionally include this
        return Response({'message': 'Signup endpoint. Submit user data via POST.'})

class login_view(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        # Χρησιμοποίησε τον UserLoginSerializer για επικύρωση των δεδομένων
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Πάρε τα επικυρωμένα δεδομένα
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')

        # Αυθεντικοποίησε τον χρήστη
        user = authenticate(request, email=email, password=password)
        if user is not None:
            # Αν ο χρήστης είναι έγκυρος, κάνε login και ανακατεύθυνέ τον
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect("home")  # Redirect στο home page
        else:
            # Επιστροφή σφάλματος αν τα credentials είναι λάθος
            return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request, *args, **kwargs):
        # Προαιρετική μέθοδος GET
        return Response({'message': 'Login endpoint. Submit email and password via POST.'})



def home(request):
    return render(request, 'home.html')



    


