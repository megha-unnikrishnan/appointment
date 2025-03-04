from datetime import time
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Appointment
from .serializers import AppointmentSerializer

# Define available time slots excluding break (1:00 PM - 2:00 PM)
AVAILABLE_SLOTS = [
    time(10, 0), time(10, 30), time(11, 0), time(11, 30),
    time(12, 0), time(12, 30), time(2, 0), time(2, 30),
    time(3, 0), time(3, 30), time(4, 0), time(4, 30)
]

@api_view(['GET'])
def available_slots(request, date):
    """Returns available slots for a given date."""
    try:
        date = date.strip()  
        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)

    # Get booked slots for the given date
    booked_slots = Appointment.objects.filter(date=date_obj).values_list('time_slot', flat=True)
    
    # Filter available slots
    available_slots = [slot.strftime('%H:%M') for slot in AVAILABLE_SLOTS if slot not in booked_slots]
    
    return Response({"available_slots": available_slots})


from datetime import datetime
@api_view(['POST'])
def book_appointment(request):
    """Allows a user to book an available slot."""
    serializer = AppointmentSerializer(data=request.data)

    if serializer.is_valid():
        date = serializer.validated_data['date']
        time_slot = serializer.validated_data['time_slot'] 

        # Check if selected slot is valid
        if time_slot not in AVAILABLE_SLOTS:
            return Response({"error": "Invalid slot selected"}, status=status.HTTP_400_BAD_REQUEST)

        # Prevent double booking
        if Appointment.objects.filter(date=date, time_slot=time_slot).exists():
            return Response({"error": "Slot already booked"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
