
# PART 1: LIST COMPREHENSIONS:

# Syntax
# [expression for item in collection]

# 1. Basic list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in numbers]
print("Squares:", squares)

# 2. List comprehension with condition
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even_numbers)

# 3. List comprehension with if-else
number_type = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print("Number types:", number_type)

# 4. List comprehension with strings
names = ["pooja", "amit", "rahul"]
uppercase_names = [name.upper() for name in names]
print("Uppercase names:", uppercase_names)

# 5. List comprehension with string condition
long_names = [name for name in names if len(name) > 4]
print("Long names:", long_names)

# 6. List comprehension using range()
squares_1_to_10 = [x ** 2 for x in range(1, 11)]
print("Squares 1 to 10:", squares_1_to_10)

# 7. List comprehension with list of dictionaries
employees = [
    {"name": "Pooja", "salary": 60000, "department": "Data Science"},
    {"name": "Amit", "salary": 45000, "department": "IT"},
    {"name": "Rahul", "salary": 70000, "department": "Data Science"},
    {"name": "Neha", "salary": 50000, "department": "HR"}
]
employee_names = [employee["name"] for employee in employees]
print("Employee names:", employee_names)

# 8. Filter employees by salary
high_salary_employees = [
    employee["name"]
    for employee in employees
    if employee["salary"] > 50000
]

print("High salary employees:", high_salary_employees)


# 9. Filter employees by department
data_science_employees = [
    employee["name"]
    for employee in employees
    if employee["department"] == "Data Science"
]

print("Data Science employees:", data_science_employees)


# 10. Create a salary list
salary_list = [employee["salary"] for employee in employees]
print("Salary list:", salary_list)

# PART 2: DICTIONARY AND SET COMPREHENSIONS

# 11. Dictionary comprehension
numbers = [1, 2, 3, 4, 5]
square_dictionary = {x: x ** 2 for x in numbers}
print("Square dictionary:", square_dictionary)


# 12. Dictionary comprehension with condition
high_salary_map = {
    employee["name"]: employee["salary"]
    for employee in employees
    if employee["salary"] > 50000
}
print("High salary map:", high_salary_map)

# 13. Set comprehension
numbers_with_duplicates = [1, 2, 2, 3, 3, 4, 4]
unique_squares = {x ** 2 for x in numbers_with_duplicates}
print("Unique squares:", unique_squares)

# PART 3: NESTED LIST COMPREHENSION

# 14. Flatten a nested list
matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
flattened = [value for row in matrix for value in row]
print("Flattened list:", flattened)



