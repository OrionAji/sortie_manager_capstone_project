from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta

class Aircraft(models.Model):
    STATUS_CHOICES = [
        ('MC', 'Mission Capable'),
        ('GND', 'Grounded'),
        ('MAINT', 'In Maintenance'),
    ]
    tail_number = models.CharField(max_length=10, unique=True)
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='MC')
    airframe_hours = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.tail_number} - {self.get_status_display()}"

class Pilot(models.Model):
    callsign = models.CharField(max_length=50, unique=True)
    rank = models.CharField(max_length=20)
    total_hours = models.DecimalField(max_digits=10, decimal_places=2)
    last_mission_end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.rank} {self.callsign}"

class Sortie(models.Model):
    TYPE_CHOICES = [
        ('NIGHT', 'Night Flying'),
        ('FORM', 'Formation'),
        ('GH', 'General Handling'),
        ('IF', 'Instrument Flight'),
    ]

    mission_id = models.CharField(max_length=20, unique=True)
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, related_name='sorties')
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE, related_name='sorties')
    sortie_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='GH')
    scheduled_at = models.DateTimeField(default=timezone.now)
    is_completed = models.BooleanField(default=False)
    is_instructional = models.BooleanField(default=False) # Added for currency bypass

    def clean(self):
    errors = {} # Use a dictionary to collect errors

    # 1. Check Aircraft Status
    if self.aircraft.status != 'MC':
        errors['aircraft'] = f"Aircraft {self.aircraft.tail_number} is {self.aircraft.get_status_display()}."
    
    # 2. Check Pilot Rest Period
    if self.pilot.last_mission_end:
        if (timezone.now() - self.pilot.last_mission_end).total_seconds() < 43200:
            errors['pilot_rest'] = "Pilot has not met the mandatory 12-hour rest period."

    # 3. Check Currency Rules
    # ... (your currency logic here) ...
    if total_flights > 0 and not recent_flight_exists and not self.is_instructional:
        errors['currency'] = f"Pilot {self.pilot.callsign} is out of currency for {self.get_sortie_type_display()}."
        

    # If the dictionary isn't empty, throw all errors at once
    if errors:
        raise ValidationError(errors)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Mission {self.mission_id} - {self.pilot.callsign}"