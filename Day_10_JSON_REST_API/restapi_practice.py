# DAY 10: REST(Representational State Transfer) API(Application Programming Interface) PRACTICE
# REST API allows applications to communicate using HTTP(HyperText Transfer Protocol)
# GET    -> Read data
# POST   -> Create data
# PUT    -> Update data
# DELETE -> Delete data

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create FastAPI application
app = FastAPI()


# Define the structure of employee data
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


# GET - Get all employees
@app.get("/employees")
def get_employees():
    return employees
# restapi it automatically convert the python data into json

# GET - Get one employee using ID
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):

    for employee in employees:
        if employee["id"] == employee_id:
            return employee

    raise HTTPException(                 # raise : Stop normal execution and generate an error.
        status_code=404,                 # HTTPException : Creates an HTTP error response.
        detail="Employee not found"
    )


# POST - Create a new employee
@app.post("/employees")
def create_employee(employee: Employee):

    new_employee = {
        "id": len(employees) + 1,
        **employee.model_dump()       # model_dump() converts that Pydantic model into a normal Python dictionary.
    }                                 # ** : This is dictionary unpacking.
# ** takes the key-value pairs from the dictionary and puts them into the new dictionary.
    employees.append(new_employee)

    return new_employee


# PUT - Update an existing employee
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

            return existing_employee

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


# DELETE - Delete an employee
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