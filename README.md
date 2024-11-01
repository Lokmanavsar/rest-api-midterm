# Student CRUD API

This project demonstrates a simple REST API built with Python's Flask framework. The API performs CRUD (Create, Read, Update, Delete) operations on student data, which can be tested locally.

## Features

- Retrieve all students
- Retrieve a specific student by ID
- Create a new student
- Update an existing student
- Delete a student

## Prerequisites

Before you can run this app, you need to have the following installed:

- Python 3.x
- pip (Python package manager)
- Flask (`pip install Flask`)
- gunicorn (`pip install gunicorn`)

## Project Structure

- `app.py`: Main Flask application 
- `requirements.txt`: List of Python dependencies 
- `test-api.http`: Test the REST API using the REST Client extension in Visual Studio Code
- `README.md`: Documentation

## Running Locally

To run the Flask API on your local machine:

1. Clone this repository:

   ```bash
   git clone https://github.com/Lokmanavsar/rest-api-midterm.git


2. Navigate to the project directory:

cd student-crud-api


3. Install the dependencies:

pip install -r requirements.txt


4. Run the application:

python app.py

5. The API will be running at http://127.0.0.1:8000.


6. Use test-api.http to test the REST API using the REST Client extension in Visual Studio Code.

### API Endpoints
GET /students: Retrieve a list of all students.
GET /students/{id}: Retrieve details of a student by ID.
POST /students: Add a new student.
PUT /students/{id}: Update an existing student by ID.
DELETE /students/{id}: Delete a student by ID.