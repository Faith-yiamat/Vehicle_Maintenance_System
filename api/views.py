from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from vehicle.models import Vehicle
from maintenance.models import MaintenanceTask
from .serializers import VehicleSerializer, MaintenanceTaskSerializer

# 🚗 Vehicle CRUD API
class VehicleListCreateView(APIView):
    def get(self, request):
        """Retrieve all vehicles"""
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Create a new vehicle"""
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VehicleDetailView(APIView):
    def get(self, request, pk):
        """Retrieve a single vehicle"""
        vehicle = get_object_or_404(Vehicle, pk=pk)
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        """Update a vehicle"""
        vehicle = get_object_or_404(Vehicle, pk=pk)
        serializer = VehicleSerializer(vehicle, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete a vehicle"""
        vehicle = get_object_or_404(Vehicle, pk=pk)
        vehicle.delete()
        return Response({"message": "Vehicle deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

# 🛠 Maintenance Task CRUD API
class MaintenanceTaskListCreateView(APIView):
    def get(self, request):
        """Retrieve all maintenance tasks"""
        tasks = MaintenanceTask.objects.all()
        serializer = MaintenanceTaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Create a new maintenance task"""
        serializer = MaintenanceTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MaintenanceTaskDetailView(APIView):
    def get(self, request, pk):
        """Retrieve a specific maintenance task"""
        task = get_object_or_404(MaintenanceTask, pk=pk)
        serializer = MaintenanceTaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        """Update a maintenance task"""
        task = get_object_or_404(MaintenanceTask, pk=pk)
        serializer = MaintenanceTaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete a maintenance task"""
        task = get_object_or_404(MaintenanceTask, pk=pk)
        task.delete()
        return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
