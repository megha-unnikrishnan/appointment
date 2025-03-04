from django.db import models


class Appointment(models.Model):
    name = models.CharField(max_length=255)  # Name of the user
    phone_number = models.CharField(max_length=15)  # User's phone number
    date = models.DateField()  # Date of appointment
    time_slot = models.TimeField(unique=True)  # Unique time slot to prevent double booking
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} - {self.date} {self.time_slot}"
