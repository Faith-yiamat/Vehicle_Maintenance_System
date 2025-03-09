from rest_framework import serializers
from vehicle.models import Vehicle
from maintenance.models import MaintenanceTask

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class MaintenanceTaskSerializer(serializers.ModelSerializer):
    vehicle_plate_number = serializers.ReadOnlyField(source="vehicle.plate_number")

    class Meta:
        model = MaintenanceTask
        fields = '__all__'
