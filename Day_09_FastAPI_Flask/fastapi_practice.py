from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Routes / Endpoints
@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}

@app.get("/hello")
def hello():
    return {"message": "Hello from my API"}

# Path Parameters
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    return {
        "employee_id": employee_id,
        "message": "Employee found"
    }

# Query Parameters
@app.get("/search")
def search_employee(department: str = None):
    return {
        "department": department,
        "message": "Search completed"
    }

# POST Request:
# {
#     "name": "Pooja",
#     "department": "IT",
#     "salary": 80000
# }

# Pydantic Model
class Employee(BaseModel):
    name: str
    department: str
    salary: float

# Create post api
@app.post("/employees")
def create_employee(employee: Employee):
    return {
        "message": "Employee created",
        "employee": employee
    }

# PUT request
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: Employee):
    return {
        "message": "Employee updated",
        "employee_id": employee_id,
        "employee": employee
    }

# DELETE Request
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    return {
        "message": "Employee deleted",
        "employee_id": employee_id
    }    

#| Code | Meaning 
#| 200 | Success 
#| 201 | Created 
#| 400 | Bad request
#| 404 | Not found
#| 500 | Server error

# Handling Errors
@app.get("/employee/{employee_id}")
def find_employee(employee_id: int):

    if employee_id != 101:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )

    return {
        "employee_id": 101,
        "name": "Amit"
    }