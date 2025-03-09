### Vehicle_Maintenance_System
## Introduction
The Vehicle Maintenance Tracking API is a RESTful API designed for a bus company to track and manage maintenance tasks performed on their fleet of vehicles. This system ensures efficient record-keeping, improved maintenance planning, and regulatory compliance.

## Project Structure
vehicle-maintenance/
│── api/                 # Contains views, serializers, and URLs for the API
│── maintenance/         # Maintenance app for tracking tasks
│── vehicle/             # Vehicle app for storing vehicle details
│── vehicle_maintenance/ # Main project settings and configurations
│── manage.py            # Django project manager
│── db.sqlite3           # SQLite database
└── README.md            # Project documentation
## Features
Log maintenance tasks for vehicles.
✅ Retrieve a list of all recorded maintenance tasks.
✅ View details of a specific maintenance task by ID.
✅ Update an existing maintenance task.
✅ Delete a maintenance task if recorded incorrectly.
✅ Retrieve a list of vehicles.

## API Endpoints
 # Maintenance Tasks
Method	Endpoint	Description
POST	/api/tasks/	Create a new maintenance task.
GET	/api/tasks/	Retrieve a list of all maintenance tasks.
GET	/api/tasks/{id}/	Retrieve details of a specific task.
PATCH	/api/tasks/{id}/	Update an existing maintenance task.
DELETE	/api/tasks/{id}/	Delete a maintenance task.
 # Vehicles
Method	Endpoint	Description
POST	/api/vehicles/	Register a new vehicle.
GET	/api/vehicles/	Retrieve all vehicles.
GET	/api/vehicles/{id}/	Get a specific vehicle.

