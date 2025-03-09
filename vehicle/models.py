from django.db import models

class Vehicle(models.Model):
    plate_number = models.CharField(max_length=20, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    is_maintenance_required = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.plate_number} - {self.make} {self.model}"
