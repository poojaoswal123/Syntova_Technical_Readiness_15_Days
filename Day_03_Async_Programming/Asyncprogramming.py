# DAY 3: ASYNCHRONOUS PROGRAMMING

# Asynchronous programming allows a program to work on other tasks
# while waiting for an operation such as an API, database,
# network or file operation.

# Synchronous:
# Task 1 -> wait -> finish -> Task 2

# Asynchronous:
# Task 1 -> waiting
# Task 2 -> can run while Task 1 is waiting

# asyncio is Python's built-in library for asynchronous programming.

import asyncio


# 1. Basic Async Function

# An async function is created using async def.
# asyncio.run() is used to execute an async function.

async def greet():
    print("Hello from async function")

asyncio.run(greet())


# 2. Using await

# await is used inside an async function.
# It waits for an asynchronous operation to complete.
# While waiting, the event loop can handle other tasks.

async def process_data():

    print("Processing started")

    await asyncio.sleep(1)

    print("Processing completed")

asyncio.run(process_data())


# 3. asyncio.sleep()

# asyncio.sleep() pauses the current async task without
# blocking the entire event loop.
#
# It can simulate waiting for:
# API response
# Database response
# Network operation
# File operation

async def wait_example():

    print("Waiting started")

    await asyncio.sleep(2)

    print("Waiting completed")

asyncio.run(wait_example())


# 4. Async Function with Parameters

# Async functions can accept parameters just like normal functions.

async def get_user(user_id):

    await asyncio.sleep(1)

    return {
        "id": user_id,
        "name": "Pooja"
    }

async def main_user():

    user = await get_user(101)

    print("User:", user)

asyncio.run(main_user())


# 5. Async Function Returning Data

# Async functions can return values using return.
# The returned value is received using await.

async def get_sales():

    await asyncio.sleep(1)

    return [1200, 1500, 1800, 2100]

async def main_sales():

    sales = await get_sales()

    total = sum(sales)

    print("Sales:", sales)
    print("Total Sales:", total)

asyncio.run(main_sales())


# 6. Sequential Async Execution

# If we use await one after another, the operations execute
# sequentially.

# Task 1 finishes first.
# Then Task 2 starts.

# Async does not automatically mean concurrent.

async def task1():

    print("Task 1 started")

    await asyncio.sleep(2)

    print("Task 1 completed")

async def task2():

    print("Task 2 started")

    await asyncio.sleep(2)

    print("Task 2 completed")

async def main_sequential():

    await task1()
    await task2()

asyncio.run(main_sequential())


# 7. asyncio.gather()

# asyncio.gather() is used to run multiple independent asynchronous operations concurrently.

# Example:
# Fetch users
# Fetch products
# Fetch orders

async def task3():

    print("Task 3 started")

    await asyncio.sleep(2)

    print("Task 3 completed")

    return "Task 3 result"

async def task4():

    print("Task 4 started")

    await asyncio.sleep(2)

    print("Task 4 completed")

    return "Task 4 result"

async def main_gather():

    result1, result2 = await asyncio.gather(
        task3(),
        task4()
    )

    print(result1)
    print(result2)

asyncio.run(main_gather())


# 8. Multiple Async Operations

# Independent API or database operations can be executed concurrently using asyncio.gather().

async def fetch_users():

    await asyncio.sleep(2)

    return ["Pooja", "Amit", "Rahul"]

async def fetch_products():

    await asyncio.sleep(2)

    return ["Laptop", "Phone", "Keyboard"]

async def fetch_orders():

    await asyncio.sleep(2)

    return [101, 102, 103]

async def main_data():

    users, products, orders = await asyncio.gather(
        fetch_users(),
        fetch_products(),
        fetch_orders()
    )

    print("Users:", users)
    print("Products:", products)
    print("Orders:", orders)

asyncio.run(main_data())


# 9. asyncio.create_task()

# asyncio.create_task() schedules an async function as a Task.
# It is useful when we want to start an async operation and
# keep a reference to that task.

async def send_email():

    await asyncio.sleep(2)

    return "Email sent successfully"

async def generate_report():

    await asyncio.sleep(1)

    return "Report generated successfully"

async def main_tasks():

    email_task = asyncio.create_task(send_email())

    report_task = asyncio.create_task(generate_report())

    email_result = await email_task
    report_result = await report_task

    print(email_result)
    print(report_result)

asyncio.run(main_tasks())


# 10. Event Loop
# The event loop manages and schedules asynchronous tasks.
# When one task is waiting for an I/O operation,
# the event loop can allow another task to run.
# asyncio.run() creates and manages the event loop for
# a normal asyncio program.

async def api1():

    await asyncio.sleep(2)

    return "API 1 data"

async def api2():

    await asyncio.sleep(3)

    return "API 2 data"

async def main_event_loop():

    results = await asyncio.gather(
        api1(),
        api2()
    )

    print("API Results:", results)

asyncio.run(main_event_loop())


# 11. Async Error Handling

# Normal try-except can be used with async functions.
# Errors raised inside async functions can be handled
# using try-except.

async def process_payment():

    await asyncio.sleep(1)

    raise ValueError("Payment failed")

async def main_error():

    try:
        await process_payment()

    except ValueError as error:
        print("Error:", error)

asyncio.run(main_error())


# 12. Async try-except-finally

# try-except-finally works with async functions just like
# normal Python functions.
#
# finally executes whether an error occurs or not.

async def connect_database():

    print("Connecting to database...")

    await asyncio.sleep(1)

    raise ConnectionError("Database connection failed")

async def main_database():

    try:
        await connect_database()

    except ConnectionError as error:
        print("Error:", error)

    finally:
        print("Connection process completed")

asyncio.run(main_database())


# 13. Error Handling with gather()

# Multiple async operations can be executed using gather().
# Exceptions can be handled using try-except.

async def get_valid_data():

    await asyncio.sleep(1)

    return "Data received"

async def get_invalid_data():

    await asyncio.sleep(1)

    raise ValueError("Invalid data")

async def main_gather_error():

    try:

        result1, result2 = await asyncio.gather(
            get_valid_data(),
            get_invalid_data()
        )

        print(result1)
        print(result2)

    except ValueError as error:

        print("Error:", error)

asyncio.run(main_gather_error())


# 14. Timeout

# Sometimes an API, database or network operation takes too long.
# asyncio.wait_for() allows us to set a maximum waiting time.
# If the operation exceeds the timeout,
# asyncio.TimeoutError is raised.

async def long_task():

    print("Task started")

    await asyncio.sleep(5)

    print("Task completed")

async def main_timeout():

    try:

        await asyncio.wait_for(
            long_task(),
            timeout=2
        )

    except asyncio.TimeoutError:

        print("Task took too long")

asyncio.run(main_timeout())


# 15. Async Loop

# Normal loops can be used inside async functions.
# await can be used inside the loop to allow the event loop
# to handle other asynchronous tasks.

async def display_numbers():

    for number in range(1, 6):

        print(number)

        await asyncio.sleep(0.5)

asyncio.run(display_numbers())


# 16. Concurrent Data Processing

# Multiple items can be processed concurrently by creating
# tasks and then using asyncio.gather().

async def process_item(item):

    await asyncio.sleep(1)

    return f"{item} processed"

async def main_processing():

    items = [
        "Sales",
        "Orders",
        "Customers",
        "Products"
    ]

    tasks = [
        asyncio.create_task(process_item(item))
        for item in items
    ]

    results = await asyncio.gather(*tasks)

    for result in results:

        print(result)

asyncio.run(main_processing())


# 17. Practical API-Style Example

# Imagine an application needs data from three APIs:
#
# API 1 -> Users
# API 2 -> Products
# API 3 -> Orders
#
# These operations are independent, so they can run
# concurrently using asyncio.gather().
#
# asyncio.sleep() represents the time taken by an API request.

async def get_api_users():

    await asyncio.sleep(2)

    return [
        {"id": 1, "name": "Pooja"},
        {"id": 2, "name": "Amit"}
    ]

async def get_api_products():

    await asyncio.sleep(2)

    return [
        {"id": 101, "name": "Laptop"},
        {"id": 102, "name": "Phone"}
    ]

async def get_api_orders():

    await asyncio.sleep(2)

    return [
        {"id": 1001, "user_id": 1},
        {"id": 1002, "user_id": 2}
    ]

async def main_api():

    users, products, orders = await asyncio.gather(
        get_api_users(),
        get_api_products(),
        get_api_orders()
    )

    print("Users:", users)
    print("Products:", products)
    print("Orders:", orders)

asyncio.run(main_api())


# 18. Mini Project: Async Student Data Fetcher

# This mini project combines the main concepts of Day 3.
#
# We need to fetch:
# Students
# Courses
# Marks
#
# All three operations are independent, so gather()
# can execute them concurrently.

async def fetch_students():

    await asyncio.sleep(1)

    return [
        {"id": 1, "name": "Pooja"},
        {"id": 2, "name": "Amit"},
        {"id": 3, "name": "Rahul"}
    ]

async def fetch_courses():

    await asyncio.sleep(1)

    return [
        "Python",
        "SQL",
        "Machine Learning"
    ]

async def fetch_marks():

    await asyncio.sleep(1)

    return [
        85,
        78,
        92
    ]

async def main_student_project():

    students, courses, marks = await asyncio.gather(
        fetch_students(),
        fetch_courses(),
        fetch_marks()
    )

    print("Students:", students)
    print("Courses:", courses)
    print("Marks:", marks)

asyncio.run(main_student_project())


# 19. Important Difference

# Sequential:

# await task1()
# await task2()

# Task 1 finishes before Task 2 starts.

# Concurrent:
# await asyncio.gather(
#     task1(),
#     task2()
# )

# Independent operations can run concurrently.


# 20. Final Summary

# async def
# Creates an asynchronous function.

# await
# Waits for an asynchronous operation.

# asyncio.run()
# Runs an asynchronous program.

# asyncio.sleep()
# Simulates asynchronous waiting.

# asyncio.gather()
# Runs multiple independent async operations concurrently.

# asyncio.create_task()
# Schedules an async function as a Task.

# Event Loop
# Manages and schedules asynchronous tasks.

# try-except
# Handles errors in asynchronous operations.

# asyncio.wait_for()
# Adds a timeout to an asynchronous operation.

# Async programming is mainly useful for I/O-bound tasks
# such as APIs, databases, networking and file operations.