from django.shortcuts import render , get_object_or_404
from .serializers import DogSerializer
from . models import Dog
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class DogView(APIView):
    serializer_class=DogSerializer

    def get(self, request , pk = None):
        if pk:
            dog = get_object_or_404(Dog , owner=request.user, pk=pk)
            serializer = DogSerializer(dog)
            return Response(serializer.data)
        else:
            dogs = Dog.objects.filter(owner=request.user)
            serializer = DogSerializer(dogs, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self , request, pk):
        dog = get_object_or_404(Dog , pk=pk)
        serializer = DogSerializer(dog , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self , request , pk):
        dog = get_object_or_404(Dog, pk=pk , owner=request.user)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
 