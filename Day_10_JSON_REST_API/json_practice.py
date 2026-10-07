# DAY 10: JSON
# JSON = JavaScript Object Notation
# Used to store and exchange data between applications and APIs

import json

# 1. Python Dictionary

employee = {
    "id": 101,
    "name": "Amit",
    "department": "IT",
    "salary": 75000,
    "skills": ["Python", "SQL", "PostgreSQL"],
    "is_active": True
}

print("Python Dictionary:")
print(employee)


# 2. Convert Python to JSON
# json.dumps() converts a Python object into a JSON string

json_data = json.dumps(employee, indent=4)

print("Python to JSON:")
print(json_data)


# 3. Convert JSON to Python
# json.loads() converts a JSON string into a Python object

python_data = json.loads(json_data)

print("JSON to Python:")
print(python_data)


# 4. Access JSON/Python Data

print("Accessing Data:")
print("Name:", python_data["name"])
print("Department:", python_data["department"])
print("Salary:", python_data["salary"])
print("First Skill:", python_data["skills"][0])


# 5. JSON Data Types
# String, Number, Boolean, Array, Object and Null

json_example = {
    "name": "Pooja",
    "age": 22,
    "is_student": True,
    "skills": ["Python", "SQL"],
    "address": {
        "city": "Kolhapur",
        "state": "Maharashtra"
    },
    "middle_name": None
}

print("JSON Data Types:")
print(json.dumps(json_example, indent=4))
# json.dumps = python to json string

# 6. Access Nested JSON Data

print("Nested Data:")
print("City:", json_example["address"]["city"])
print("State:", json_example["address"]["state"])


# 7. Save Python Data to JSON File
# json.dump() writes Python data directly into a JSON file

with open("employee.json", "w") as file:
    json.dump(employee, file, indent=4)  # json.dump = python to json file

print("Data saved to employee.json")


# 8. Read JSON File
# json.load() reads JSON data from a file and converts it to Python

with open("employee.json", "r") as file:
    loaded_employee = json.load(file)
# json.load() reads the JSON file and converts the data into a Python object
print("Data read from employee.json:")
print(loaded_employee)


# 9. Update JSON/Python Data

loaded_employee["salary"] = 80000
loaded_employee["city"] = "Pune"

print("Updated Data:")
print(loaded_employee)


# 10. Convert Updated Data to JSON

updated_json = json.dumps(loaded_employee, indent=4)

print("Updated JSON:")
print(updated_json)


# Important JSON Functions
# json.dumps() -> Python to JSON string
# json.loads() -> JSON string to Python
# json.dump()  -> Python to JSON file
# json.load()  -> JSON file to Python