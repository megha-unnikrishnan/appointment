

from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Appointment  # Ensure your model is correctly imported

# Define available slots (Example: Every hour from 9 AM to 5 PM)
AVAILABLE_SLOTS = [
    datetime.strptime(f"{hour}:00", "%H:%M").time() for hour in range(9, 18)
]

@api_view(["GET"])
def available_slots(request):
    """Returns available and booked time slots for a given date."""
    date_str = request.GET.get("date")  # Get date parameter from request

    if not date_str:
        return Response({"error": "Date parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()  # Convert string to date
    except ValueError:
        return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

    # Get booked slots from database
    booked_slots = list(Appointment.objects.filter(date=date).values_list("time_slot", flat=True))

    # Ensure all booked slots are formatted correctly
    booked_slots = [datetime.strptime(slot, "%H:%M").time() if isinstance(slot, str) else slot for slot in booked_slots]
    booked_slots = [slot.strftime("%H:%M") for slot in booked_slots]

    # Determine available slots
    available_slots = [slot.strftime("%H:%M") for slot in AVAILABLE_SLOTS if slot.strftime("%H:%M") not in booked_slots]

    return Response({
        "available_slots": available_slots,
        "booked_slots": booked_slots
    }, status=status.HTTP_200_OK)


@api_view(["POST"])
def book_appointment(request):
    """Books an appointment if the slot is available."""
    data = request.data
    name = data.get("name")
    phone_number = data.get("phone_number")
    date_str = data.get("date")
    time_slot_str = data.get("time_slot")

    if not all([name, phone_number, date_str, time_slot_str]):
        return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        time_slot = datetime.strptime(time_slot_str, "%H:%M").time()
    except ValueError:
        return Response({"error": "Invalid time format. Use HH:MM."}, status=status.HTTP_400_BAD_REQUEST)

    # 🚨 **Check if the slot is already booked**
    if Appointment.objects.filter(date=date, time_slot=time_slot).exists():
        return Response({"error": "Selected time slot is already booked."}, status=status.HTTP_400_BAD_REQUEST)

    # Save appointment only if the slot is available
    Appointment.objects.create(name=name, phone_number=phone_number, date=date, time_slot=time_slot)

    return Response({"message": "Appointment booked successfully!"}, status=status.HTTP_201_CREATED)
