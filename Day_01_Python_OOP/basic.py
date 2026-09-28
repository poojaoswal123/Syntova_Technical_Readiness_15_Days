# variable and data type
name = "Pooja" # str
age = 22 # int
college = "SGU" # str
cgpa = 86.4 # float
is_student = True # bool
result = None # NoneType
# print
print(name, type(name))
print(age, type(age))
print(college, type(college))
print(cgpa, type(cgpa))
print(is_student, type(is_student))

# TYPE CONVERSION
age = "22"
print(type(age))
age = int(age)
print(type(age))

# OPERATORS
a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b) # division 
print(a%b) # remainder eg 10/3 remainder is 1
print(a**b) # power (Raises the first number to the power of the second number) here 10 × 10 × 10
print(a//b) # floor division : Performs division and returns the floor value 10//3 = 3

# COMPARISON OPERATORS
# ==, !=, >, <, >=, <=

# = means assignment         age = 22
# == means comparison.       age == 22

a = 10
b = 20
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a >= b)
print(a <= b)

# LOGICAL OPERATORS : and , or, not
# AND : Both conditions must be true.
age = 22
salary = 60000
if age >= 18 and salary >= 50000:
    print("Eligible")
else:
    print("Not Eligible")

# OR : At least one condition must be true.
age = 17
salary = 60000
if age >= 18 or salary >= 50000:
    print("Eligible")
else:
    print("Not Eligible")    

# NOT: Reverses the result.
is_active = False
print(not is_active)    

# user input
name = input("Enter your name: ")
print(name)
age = int(input("Enter age: "))
print(age)

# f string
name = "Pooja"
age = 22
print(f"My name is {name} and I am {age} years old")

# example
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"I live in {city}.")

# CONDITIONAL STATEMENTS
# if
age = 22
if age >= 18:
    print("Adult")

# if else
age = 16
if age >= 18:
    print("Adult")
else:
    print("Not an Adult")

# if elif else
marks = 85
if marks>=90:
    print("A")
elif marks>=75:
    print("B")
elif marks>=60:
    print("C")
else:
    print("D")

# practice questions:
# Even odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd") 

# positive / negative /0
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# Largest of 2 numbers
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if a > b :
    print("First number is larger")
elif b > a:
    print("Second number is larger")
else :
    print("Both are equal")



    