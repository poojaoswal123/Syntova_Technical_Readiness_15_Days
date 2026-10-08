
# DAY 11: HTTP REQUEST LIFECYCLE
# Basic to Intermediate FastAPI Practice

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel

app = FastAPI()


# Employee request model
class Employee(BaseModel):
    name: str
    department: str
    salary: float


# Sample employee data
employees = [
    {
        "id": 1,
        "name": "Amit",
        "department": "IT",
        "salary": 75000
    },
    {
        "id": 2,
        "name": "Pooja",
        "department": "Data",
        "salary": 80000
    }
]


# Basic endpoint
@app.get("/")
def home():
    return {
        "message": "HTTP API is working"
    }


# Inspect the incoming HTTP request
@app.get("/request-info")
async def request_info(request: Request): 

    return {
        "method": request.method, # request.method tells us which HTTP method was used(GET ,POST,PUT,DELETE)
        "url": str(request.url), # Take the complete URL from the incoming request, convert it to a string, and put it in the response under the key url
        "path": request.url.path, # This extracts only the path. eg: http://127.0.0.1:8000/request-info    the path is: /request-info
        "query_parameters": dict(request.query_params), # if we req /request-info?department=Data  here department=Data this is query parameter
        "headers": dict(request.headers) # contain info like (User-Agent ,Host, Accept, Content-Type)
    }


# GET - Get all employees
@app.get("/employees")
def get_employees():
    return employees


# GET - Get employee using path parameter
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):

    for employee in employees:

        if employee["id"] == employee_id:
            return employee

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


# GET - Search using query parameter
@app.get("/search")
def search_employee(department: str = None):

    if department is None:
        return employees

    result = []

    for employee in employees:

        if employee["department"].lower() == department.lower():
            result.append(employee)

    return result


# POST - Create employee
@app.post("/employees", status_code=201)
def create_employee(employee: Employee):

    new_employee = {
        "id": len(employees) + 1,
        **employee.model_dump() # model_dump() converts the Pydantic object into a dictionary
    }

    employees.append(new_employee)

    return {
        "message": "Employee created successfully",
        "employee": new_employee
    }


# PUT - Update employee
@app.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    employee: Employee
):

    for existing_employee in employees:

        if existing_employee["id"] == employee_id:

            existing_employee.update(
                employee.model_dump()
            )

            return {
                "message": "Employee updated successfully",
                "employee": existing_employee
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


# DELETE - Delete employee
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):

    for employee in employees:

        if employee["id"] == employee_id:

            employees.remove(employee)

            return {
                "message": "Employee deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


# Demonstrate 400 Bad Request
@app.get("/check/{employee_id}")
def check_employee(employee_id: int):

    if employee_id <= 0:

        raise HTTPException(
            status_code=400,
            detail="Employee ID must be greater than 0"
        )

    return {
        "message": "Employee ID is valid",
        "employee_id": employee_id
    }


# 200 → Success
# 201 → Created
# 400 → Bad Request
# 404 → Not Found
# 500 → Server Error