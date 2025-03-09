from django.db import models
from vehicle.models import Vehicle

class MaintenanceTask(models.Model):
    TASK_CHOICES = [
        ('oil_change', 'Oil Change'),
        ('brake_inspection', 'Brake Inspection'),
        ('tire_rotation', 'Tire Rotation'),
    ]

    vehicle = models.ForeignKey(Vehicle, related_name="tasks", on_delete=models.CASCADE)
    task_type = models.CharField(max_length=50, choices=TASK_CHOICES)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.vehicle.plate_number} - {self.task_type}"
