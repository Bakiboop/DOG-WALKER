from django.shortcuts import render
from django.shortcuts import render , get_object_or_404
from .serializers import DogSerializer
from . models import Dog
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class DogListView(APIView):

    def get(self, request):
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)