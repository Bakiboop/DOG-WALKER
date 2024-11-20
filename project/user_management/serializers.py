from .models import User
from .models import Person
from rest_framework import serializers
from django.contrib.auth import authenticate

class PersonSignupSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)  

    class Meta:
        model = Person
        fields = ["email", "password", "password2", "first_name", "last_name", "address", "phone_number"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Οι κωδικοί δεν ταιριάζουν.")
        return data

    def create(self, validated_data):
        validated_data.pop("password2")  
        password = validated_data.pop("password")
        
        # Δημιουργία χρήστη με κρυπτογράφηση κωδικού
        person = Person(**validated_data)
 
        person.save()
        
        return person
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    
