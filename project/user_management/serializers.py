from .models import User, Person
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class PersonSignupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=50)
    phone_number = serializers.CharField(max_length=10)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value
    
    def create(self, validated_data):
        # Αφαίρεση των πεδίων που αφορούν το προφίλ `Person`
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        address = validated_data.pop('address')
        phone_number = validated_data.pop('phone_number')
    
        # Δημιουργία του χρήστη
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
    
        # Δημιουργία και αποθήκευση του προφίλ `Person` με τα επιπλέον στοιχεία
        person = Person.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone_number=phone_number
        )
        
        return person  # Επιστρέφει το αντικείμενο Person για επιβεβαίωση
    
    
class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        user = authenticate(email=attrs.get("email"), password=attrs.get("password"))
        if not user:
            raise serializers.ValidationError("Invalid email or password")
        return {"user": user}
