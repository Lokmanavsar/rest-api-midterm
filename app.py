from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory "database" of students
students = [
    {"id": 1, "name": "John Doe", "grade": "A", "email": "john@example.com"},
    {"id": 2, "name": "Jane Smith", "grade": "B", "email": "jane@example.com"},
]

@app.route('/')
def index():
    return "Welcome to the Student Management API! Use /students to manage students."

# GET /students - Retrieve all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200

# GET /students/<id> - Retrieve a student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        abort(404)  # Not Found
    return jsonify(student), 200

# POST /students - Add a new student
@app.route('/students', methods=['POST'])
def create_student():
    if not request.json or 'name' not in request.json or 'grade' not in request.json or 'email' not in request.json:
        abort(400)  # Bad Request
    
    new_student = {
        'id': students[-1]['id'] + 1 if students else 1,
        'name': request.json['name'],
        'grade': request.json['grade'],
        'email': request.json['email']
    }
    students.append(new_student)
    return jsonify(new_student), 201  # Created

# PUT /students/<id> - Update a student by ID
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is None:
        abort(404)  # Not Found
    
    if not request.json:
        abort(400)  # Bad Request
    
    student['name'] = request.json.get('name', student['name'])
    student['grade'] = request.json.get('grade', student['grade'])
    student['email'] = request.json.get('email', student['email'])
    return jsonify(student), 200

# DELETE /students/<id> - Delete a student by ID
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [s for s in students if s['id'] != student_id]
    return '', 204  # No Content

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
