from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .services import AppointmentService
from django.core.exceptions import ValidationError
from .serializers import AppointmentBookingSerializer

class AppointmentsView(APIView):
    permission_classes=[IsAuthenticated]
    serializer_class=AppointmentBookingSerializer

    def __init__(self, appointment_service=None):
        # Inject the service manually (default to AppointmentService if not provided)
        self.appointment_service = appointment_service if appointment_service else AppointmentService()

    def get(self, request):
        try:
            # Retrieve all appointments for the current user by their primary key
            appointments = self.appointment_service.get_appointments_by_owner(request.user.id)
            serializer = AppointmentBookingSerializer(appointments, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            # Create a new appointment for the current user by their primary key
            serializer = self.appointment_service.create_appointment(request.user.id, request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            # Update an existing appointment for the current user by their primary key
            serializer = self.appointment_service.update_appointment(request.user.id, request.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            # Delete an existing appointment for the current user by their primary key
            self.appointment_service.delete_appointment(request.user.id, request.data)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)