from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .services import DogService, AppointmentService
from .serializers import DogSerializer, AppointmentBookingSerializer

class DogView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class=DogSerializer

    def __init__(self, dog_service=None):
        # Inject the service manually (default to DogService if not provided)
        self.dog_service = dog_service if dog_service else DogService()

    def get(self, request, pk=None):
        if pk:
            dog = self.dog_service.get_dog_by_id(request.user, pk)
            serializer = DogSerializer(dog)
            return Response(serializer.data)
        else:
            dogs = self.dog_service.get_dogs_by_owner(request.user)
            serializer = DogSerializer(dogs, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = self.dog_service.create_dog(request.user, request.data)
        if serializer:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        dog = self.dog_service.get_dog_by_id(request.user, pk)
        serializer = self.dog_service.update_dog(dog, request.data)
        if serializer:
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        dog = self.dog_service.get_dog_by_id(request.user, pk)
        self.dog_service.delete_dog(dog)
        return Response(status=status.HTTP_204_NO_CONTENT)

class AppointmentsView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class=AppointmentBookingSerializer
    def __init__(self, appointment_service=None):
        # Inject the service manually (default to AppointmentService if not provided)
        self.appointment_service = appointment_service if appointment_service else AppointmentService()

    def get(self, request, pk=None):
        if pk:
            appointment = self.appointment_service.get_appointment_by_id(request.user, pk)
            serializer = AppointmentBookingSerializer(appointment)
            return Response(serializer.data)
        else:
            appointments = self.appointment_service.get_appointments_by_owner(request.user)
            serializer = AppointmentBookingSerializer(appointments, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = self.appointment_service.create_appointment(request.user, request.data)
        if serializer:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        appointment = self.appointment_service.get_appointment_by_id(request.user, pk)
        serializer = self.appointment_service.update_appointment(appointment, request.data)
        if serializer:
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        appointment = self.appointment_service.get_appointment_by_id(request.user, pk)
        self.appointment_service.delete_appointment(appointment)
        return Response(status=status.HTTP_204_NO_CONTENT)