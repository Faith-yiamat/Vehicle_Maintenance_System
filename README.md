# Vehicle_Maintenance_System
## Introduction
The Vehicle Maintenance Tracking API is a RESTful API designed for a bus company to track and manage maintenance tasks performed on their fleet of vehicles. This system ensures efficient record-keeping, improved maintenance planning, and regulatory compliance.

## Project Structure
vehicle-maintenance/
│── api/                  - Contains views, serializers, and URLs for the API

│── maintenance/         -Maintenance app for tracking tasks

│── vehicle/             - Vehicle app for storing vehicle details

│── vehicle_maintenance/ - Main project settings and configurations

│── manage.py            -Django project manager

│── db.sqlite3           -SQLite database

└── README.md            -Project documentation


## Features

### Log maintenance tasks for vehicles.

✅ Retrieve a list of all recorded maintenance tasks.

✅ View details of a specific maintenance task by ID.

✅ Update an existing maintenance task.

✅ Delete a maintenance task if recorded incorrectly.

✅ Retrieve a list of vehicles.



## Setup Instructions

### Prerequisites

Ensure you have the following installed on your system:

Python 3.10+

Django & Django REST Framework

PostgreSQL (or SQLite for development)

Git

### Virtual Environment (venv)
#### 1. Clone the Repository

$ git clone https://github.com/Faith-yiamat/Vehicle_Maintenance_System.git

$ cd Vehicle_Maintenance_System

#### 2. Create and Activate a Virtual Environment

$ python -m venv env
$ source env/bin/activate   # On Windows, use `env\Scripts\activate`

#### 3. Install Dependencies

$ pip install -r requirements.txt

#### 4. Set Up the Database

Run migrations to create the necessary database tables:

$ python manage.py migrate

#### 5. Create a Superuser (For Admin Panel)

$ python manage.py createsuperuser

#### 6. Run the Development Server

$ python manage.py runserver

The API will 5. Create a Superuser (For Admin Panel)

$ python manage.py createsuperuser

be available at: http://127.0.0.1:8000/

## How to Run the API

### 1. API Endpoints

The API follows RESTful principles and provides the following endpoints:

#### Create a new maintenance task

POST /api/tasks/

{
  "vehicle": "ABC123",
  "task_type": "oil_change",
  "description": "Changed engine oil and replaced filter"
}

Response:

{
  "id": 1,
  "vehicle": "ABC123",
  "task_type": "oil_change",
  "description": "Changed engine oil and replaced filter",
  "status": "pending",
  "created_at": "2025-03-09T12:34:56Z"
}

#### Retrieve all maintenance tasks

GET /api/tasks/
Response:

[
  {
    "id": 1,
    "vehicle": "ABC123",
    "task_type": "oil_change",
    "description": "Changed engine oil and replaced filter",
    "status": "pending",
    "created_at": "2025-03-09T12:34:56Z"
  }
]

#### Retrieve a specific maintenance task

GET /api/tasks/{id}/

#### Update a maintenance task

PATCH /api/tasks/{id}/

{
  "status": "completed"
}

#### Delete a maintenance task

DELETE /api/tasks/{id}/

#### Filter tasks by vehicle registration

GET /api/tasks/?vehicle=ABC123

## Conclusion

This API provides an efficient way to manage vehicle maintenance records and ensures that tasks are logged, tracked, and retrieved easily. If you have any issues, feel free to raise an issue in the repository.


