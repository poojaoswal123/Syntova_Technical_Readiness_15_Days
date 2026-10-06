# DAY 9: FLASK
# Basic to Intermediate Practice

from flask import Flask, request

app = Flask(__name__)


# 1. Basic GET endpoint
@app.route("/")
def home():
    return {
        "message": "Hello from Flask!"
    }


# 2. Another GET endpoint
@app.route("/hello")
def hello():
    return {
        "message": "Hello from Flask API"
    }


# 3. GET with path parameter
@app.route("/employees/<int:employee_id>")
def get_employee(employee_id):
    return {
        "employee_id": employee_id,
        "message": "Employee found"
    }


# 4. GET with query parameter
@app.route("/search")
def search_employee():

    department = request.args.get("department")

    return {
        "department": department,
        "message": "Search completed"
    }


# 5. POST - create employee
@app.route("/employees", methods=["POST"])
def create_employee():

    employee = request.get_json()

    return {
        "message": "Employee created",
        "employee": employee
    }


# 6. PUT - update employee
@app.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):

    employee = request.get_json()

    return {
        "message": "Employee updated",
        "employee_id": employee_id,
        "employee": employee
    }


# 7. DELETE - delete employee
@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):

    return {
        "message": "Employee deleted",
        "employee_id": employee_id
    }


if __name__ == "__main__":
    app.run(debug=True)