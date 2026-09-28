# 1. Basic Functions

# create and call a function
def my_function():
    print("Hello from a function")

my_function()

# function with one parameter
def greet(name):
    print("Hello", name)

greet("Pooja")

# function with multiple parameters
def greet_person(first_name, last_name):
    print(first_name + " " + last_name)

greet_person("Pooja", "Oswal")

# return value
def add(x, y):
    return x + y

result = add(5, 3)
print(result)

# default parameter
def greet_default(name="friend"):
    print("Hello", name)

greet_default("Pooja")
greet_default()

# keyword arguments
def pet(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)

pet(animal="dog", name="Buddy")

# list as an argument
def print_fruits(fruits):
    for fruit in fruits:
        print(fruit)

my_fruits = ["apple", "banana", "cherry"]
print_fruits(my_fruits)

# dictionary as an argument
def print_person(person):
    print("Name:", person["name"])
    print("Age:", person["age"])

my_person = {
    "name": "Emil",
    "age": 25
}

print_person(my_person)

# function returning a list
def get_fruits():
    return ["apple", "banana", "cherry"]

fruits = get_fruits()
print(fruits)

# function returning a tuple
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()

print("x:", x)
print("y:", y)


# 2. Advanced Arguments

# *args
def show_args(*args):
    print("Type:", type(args))
    print("Arguments:", args)

show_args("Pooja", "Python", 25)

# sum using *args
def total(*numbers):
    result = 0

    for num in numbers:
        result += num

    return result

print(total(1, 2, 3))
print(total(10, 20, 30, 40))

# multiplication using *args
def multiply(*numbers):
    result = 1

    for num in numbers:
        result *= num

    return result

print(multiply(2, 3, 4))

# **kwargs
def show_kwargs(**kwargs):
    print("Type:", type(kwargs))
    print("Arguments:", kwargs)

show_kwargs(name="Pooja", age=22, city="Kolhapur")

# accessing **kwargs values
def person_info(**kwargs):
    print("Name:", kwargs["name"])
    print("Age:", kwargs["age"])

person_info(name="Pooja", age=22)

# * unpacking
def add_three(a, b, c):
    return a + b + c

numbers = [1, 2, 3]

print(add_three(*numbers))

# ** unpacking
def greet_user(first_name, last_name):
    print("Hello", first_name, last_name)

person = {
    "first_name": "Pooja",
    "last_name": "Oswal"
}

greet_user(**person)


# 3. Functions as Arguments

# passing a function as an argument
def square(x):
    return x * x

def apply(fun, value):
    return fun(value)

print(apply(square, 5))

# add function passed to another function
def add_number(num):
    return 10 + num

print(apply(add_number, 6))

# choose add or multiply
def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def calculate(fun, x, y):
    return fun(x, y)

print(calculate(add_numbers, 5, 6))
print(calculate(multiply_numbers, 5, 6))

# calculator using functions
def add_calc(x, y):
    return x + y

def difference_calc(x, y):
    return x - y

def multiply_calc(x, y):
    return x * y

def divide_calc(x, y):
    return x / y

def operate(fun, a, b):
    return fun(a, b)

print(operate(add_calc, 10, 5))
print(operate(difference_calc, 10, 5))
print(operate(multiply_calc, 10, 5))
print(operate(divide_calc, 10, 5))


# 4. Lambda Functions

# lambda with one argument
square_lambda = lambda x: x * x

print(square_lambda(5))

# lambda with two arguments
add_lambda = lambda a, b: a + b

print(add_lambda(5, 3))

# lambda for even or odd
check_even = lambda x: x % 2 == 0

print(check_even(10))
print(check_even(7))

# lambda with a function
def apply_lambda(fun, value):
    return fun(value)

print(apply_lambda(lambda x: x * 2, 5))


# 5. map()

# square every number
numbers = [1, 2, 3, 4, 5]

squares = map(lambda x: x * x, numbers)

print(list(squares))

# double every number
numbers = [1, 2, 3, 4, 5]

double = map(lambda x: x * 2, numbers)

print(list(double))

# convert strings to uppercase
names = ["pooja", "amit", "rahul"]

upper_names = map(lambda x: x.upper(), names)

print(list(upper_names))

# map with normal function
def square_num(x):
    return x * x

numbers = [2, 4, 6, 8]

result = map(square_num, numbers)

print(list(result))


# 6. filter()

# filter even numbers
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))

# filter odd numbers
numbers = [1, 2, 3, 4, 5, 6]

odd_numbers = filter(lambda x: x % 2 != 0, numbers)

print(list(odd_numbers))

# filter numbers greater than 5
numbers = [2, 5, 7, 10, 3, 8]

greater_than_five = filter(lambda x: x > 5, numbers)

print(list(greater_than_five))

# filter strings by length
names = ["Pooja", "Amit", "Rahul", "Raj"]

long_names = filter(lambda x: len(x) > 4, names)

print(list(long_names))


# 7. reduce()

from functools import reduce

# sum using reduce
numbers = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a + b, numbers)

print(result)

# multiplication using reduce
numbers = [1, 2, 3, 4, 5]

result = reduce(lambda a, b: a * b, numbers)

print(result)

# find maximum using reduce
numbers = [10, 5, 20, 8, 15]

result = reduce(lambda a, b: a if a > b else b, numbers)

print(result)


# 8. Nested Functions

# function inside another function
def outer():

    print("Outer function")

    def inner():
        print("Inner function")

    inner()

outer()

# nested function with parameters
def calculator():

    def add(a, b):
        return a + b

    print(add(10, 20))

calculator()


# 9. Closures

# closure
def outer_function(x):

    def inner_function(y):
        return x + y

    return inner_function

add_five = outer_function(5)

print(add_five(10))

# another closure example
def multiplier(x):

    def multiply(y):
        return x * y

    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))
print(triple(5))


# 10. Decorators

# basic decorator
def decorator_function(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper

@decorator_function
def say_hello():
    print("Hello")

say_hello()

# decorator with arguments
def my_decorator(func):

    def wrapper(name):
        print("Function started")
        func(name)
        print("Function ended")

    return wrapper

@my_decorator
def welcome(name):
    print("Welcome", name)

welcome("Pooja")

# decorator with *args and **kwargs
def decorator(func):

    def wrapper(*args, **kwargs):
        print("Before function")
        result = func(*args, **kwargs)
        print("After function")
        return result

    return wrapper

@decorator
def add_values(a, b):
    return a + b

print(add_values(5, 3))


# 11. Generators

# simple generator
def numbers_generator():
    yield 1
    yield 2
    yield 3

numbers = numbers_generator()

print(next(numbers))
print(next(numbers))
print(next(numbers))

# generator using loop
def count_numbers(n):

    for i in range(1, n + 1):
        yield i

for num in count_numbers(5):
    print(num)

# generator for squares
def square_generator(n):

    for i in range(1, n + 1):
        yield i * i

for square in square_generator(5):
    print(square)


# 12. Recursion

# factorial using recursion
def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

# countdown using recursion
def countdown(n):

    if n == 0:
        print("Done")
        return

    print(n)
    countdown(n - 1)

countdown(5)

# sum using recursion
def recursive_sum(n):

    if n == 0:
        return 0

    return n + recursive_sum(n - 1)

print(recursive_sum(5))

# fibonacci using recursion
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))