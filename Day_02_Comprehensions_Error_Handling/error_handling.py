# PART 4: ERROR HANDLING
# 15. Basic try-except
try:
    number = int("100")
    print("Converted number:", number)

except ValueError:
    print("Invalid number")

# 16. Handling ValueError
try:
    number = int("abc")
    print(number)

except ValueError:
    print("Invalid integer")

# 17. Handling ZeroDivisionError
try:
    result = 10 / 0
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")


# 18. Handling multiple exceptions
try:
    number = int("abc")
    result = 100 / number
    print(result)

except ValueError:
    print("Please provide a valid number")

except ZeroDivisionError:
    print("Number cannot be zero")


# 19. Getting the actual error message
try:
    result = 10 / 0

except ZeroDivisionError as error:
    print("Error:", error)


# PART 5: try-except-else-finally

# 20. else runs when there is no error
try:
    number = int("50")

except ValueError:
    print("Invalid number")

else:
    print("Successfully converted:", number)


# 21. finally always runs
try:
    number = int("100")

except ValueError:
    print("Invalid number")

finally:
    print("Operation completed")


# 22. Complete try-except-else-finally
try:
    number = int("25")
    result = 100 / number

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("Program finished")


# PART 6: COMMON PROJECT ERRORS

# 23. KeyError
employee = {
    "name": "Pooja",
    "salary": 60000
}

try:
    department = employee["department"]

except KeyError:
    print("Department is missing")


# 24. IndexError
numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError:
    print("Index does not exist")


# 25. TypeError
try:
    result = "100" + 50

except TypeError:
    print("Cannot combine string and integer")


# PART 7: ERROR HANDLING WITH FUNCTIONS

# 26. Safe division function
def divide(a, b):
    try:
        return a / b

    except ZeroDivisionError:
        return "Cannot divide by zero"

    except TypeError:
        return "Invalid data type"


print("Division:", divide(10, 2))
print("Division:", divide(10, 0))


# 27. Safe integer conversion
def convert_to_integer(value):
    try:
        return int(value)

    except ValueError:
        return "Invalid integer"


print("Conversion:", convert_to_integer("100"))
print("Conversion:", convert_to_integer("abc"))


# PART 8: raise

# 28. Using raise for validation
def check_salary(salary):

    if salary < 0:
        raise ValueError("Salary cannot be negative")

    return salary


print("Salary:", check_salary(60000))


# PART 9: ERROR HANDLING WITH LIST OF DICTIONARIES

# 29. Safely access employee salary
employees_with_missing_data = [
    {"name": "Pooja", "salary": 60000},
    {"name": "Amit"},
    {"name": "Rahul", "salary": 70000}
]


def get_salary(employee):

    try:
        return employee["salary"]

    except KeyError:
        return None


for employee in employees_with_missing_data:

    salary = get_salary(employee)

    if salary is not None:
        print(employee["name"], "Salary:", salary)

    else:
        print(employee["name"], "Salary not available")