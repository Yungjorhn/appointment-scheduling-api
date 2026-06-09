# Appointment Scheduling API

A cloud-based appointment scheduling system built with FastAPI and SQLAlchemy ORM. This API allows users to manage meetings, participants, and schedules across different geographic locations and time zones.

## Features

- User management system
- Appointment scheduling
- Time zone-aware meeting handling
- CRUD operations for meetings and participants
- RESTful API architecture
- Database integration using SQLAlchemy ORM
- Data validation using Pydantic
- Interactive API documentation with Swagger UI

## Technologies Used

- Python
- FastAPI
- SQLAlchemy ORM
- SQLite
- Pydantic

## Project Overview

This project was developed to demonstrate backend engineering concepts using FastAPI and SQLAlchemy. The system enables users from different locations and time zones to schedule and manage meetings efficiently.

The API automatically handles time zone conversions so that users can view meeting schedules in their local time zones regardless of where the meeting was created.

## API Functionalities

### User Management
- Create users
- Retrieve user details
- Update user information
- Delete users

### Appointment Management
- Schedule appointments
- Update appointment details
- Delete appointments
- Retrieve scheduled meetings

### Time Zone Handling
- Store timezone-aware meeting information
- Convert meeting schedules across different user time zones

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /users | Create a new user |
| GET | /users | Retrieve all users |
| POST | /appointments | Schedule a new appointment |
| GET | /appointments | Retrieve all appointments |
| PUT | /appointments/{id} | Update appointment details |
| DELETE | /appointments/{id} | Delete an appointment |

## Installation

Clone the repository:

```bash
git clone https://github.com/Yungjorhn/appointment-scheduling-api.git
```

Navigate into the project folder:

```bash
cd appointment-scheduling-api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
uvicorn main:app --reload
```

## API Documentation

Swagger UI documentation is available at:

```text
http://127.0.0.1:8000/docs
```

## Future Improvements

- JWT Authentication
- Email notifications
- Calendar integration
- PostgreSQL support
- Deployment using Docker

## Project Status

Completed as part of backend engineering and API development learning using FastAPI and SQLAlchemy ORM.
