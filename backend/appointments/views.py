

from datetime import datetime, time, timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Appointment  # Ensure your model is correctly imported




# Function to generate 30-minute slots (excluding 1:00 PM - 2:00 PM)
def generate_available_slots():
    start_time = time(10, 0)  
    end_time = time(17, 0)    
    break_start = time(13, 0)
    break_end = time(14, 0)   

    slots = []
    current_time = datetime.combine(datetime.today(), start_time)

    while current_time.time() < end_time:
        if not (break_start <= current_time.time() < break_end):  # Exclude break time
            slots.append(current_time.time().strftime("%H:%M"))
        current_time += timedelta(minutes=30)

    return slots

@api_view(["GET"])
def available_slots(request):
    """Returns available and booked time slots for a given date."""
    date_str = request.GET.get("date")

    if not date_str:
        return Response({"error": "Date parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

    # Get booked slots from the database
    booked_slots = list(Appointment.objects.filter(date=date).values_list("time_slot", flat=True))
    
    # Convert booked slots to string format
    booked_slots = [slot.strftime("%H:%M") for slot in booked_slots]

    # Generate available slots
    all_slots = generate_available_slots()
    available_slots = [slot for slot in all_slots if slot not in booked_slots]

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
