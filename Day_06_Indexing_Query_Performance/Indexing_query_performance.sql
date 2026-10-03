-- DAY 6: INDEXING & QUERY PERFORMANCE
-- PostgreSQL Practice


-- Create departments table
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

-- Create employees table
-- manager_id is used later for SELF JOIN
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    department_id INT,
    salary NUMERIC(10,2),
    city VARCHAR(50),
    manager_id INT
);

-- Create projects table
CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    department_id INT
);

-- Insert departments
INSERT INTO departments
(department_id, department_name)
VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Finance'),
(4, 'Marketing');

-- Insert employees
INSERT INTO employees
(employee_id, employee_name, department_id, salary, city, manager_id)
VALUES
(101, 'Amit', 1, 75000, 'Pune', NULL),
(102, 'Priya', 2, 60000, 'Mumbai', 101),
(103, 'Rahul', 1, 85000, 'Pune', 101),
(104, 'Sneha', 3, 70000, 'Kolhapur', 107),
(105, 'Neha', 1, 90000, 'Mumbai', 101),
(106, 'Kiran', 4, 65000, 'Pune', 108),
(107, 'Rohit', 3, 80000, 'Mumbai', NULL),
(108, 'Pooja', 2, 62000, 'Kolhapur', 101);

-- Insert projects
INSERT INTO projects
(project_id, project_name, department_id)
VALUES
(1, 'AI Project', 1),
(2, 'Recruitment System', 2),
(3, 'Finance Dashboard', 3),
(4, 'Marketing Website', 4);

-- Check the employees table
SELECT *
FROM employees;

-- Check existing indexes on employees
SELECT
    indexname,
    indexdef
FROM pg_indexes
WHERE tablename = 'employees';

-- Check query performance before creating an index
-- EXPLAIN shows the planned execution method
EXPLAIN
SELECT *
FROM employees
WHERE department_id = 1;

-- EXPLAIN ANALYZE
-- Executes the query and shows actual execution information
EXPLAIN ANALYZE
SELECT *
FROM employees
WHERE department_id = 1;

-- Create an index on department_id
-- Useful when department_id is frequently used for searching/filtering
CREATE INDEX IF NOT EXISTS idx_employees_department
ON employees(department_id);

--  Check the index created above
SELECT
    indexname,
    indexdef
FROM pg_indexes
WHERE tablename = 'employees';

-- Check the query plan after creating the index
EXPLAIN
SELECT *
FROM employees
WHERE department_id = 1;

-- Check actual query performance
EXPLAIN ANALYZE
SELECT *
FROM employees
WHERE department_id = 1;

-- Create an index on employee_name
CREATE INDEX IF NOT EXISTS idx_employees_name
ON employees(employee_name);

-- Search using employee_name
SELECT *
FROM employees
WHERE employee_name = 'Pooja';

-- Check performance of employee_name search
EXPLAIN ANALYZE
SELECT *
FROM employees
WHERE employee_name = 'Pooja';

-- Create an index on city
CREATE INDEX IF NOT EXISTS idx_employees_city
ON employees(city);

--  Search employees by city
SELECT *
FROM employees
WHERE city = 'Pune';

-- Check performance of city search
EXPLAIN ANALYZE
SELECT *
FROM employees
WHERE city = 'Pune';

--  Create a composite index
-- An index using more than one column
CREATE INDEX IF NOT EXISTS idx_department_salary
ON employees(department_id, salary);

-- Query using both columns
SELECT *
FROM employees
WHERE department_id = 1
AND salary > 70000;

--  Check performance of the composite-index query
EXPLAIN ANALYZE
SELECT *
FROM employees
WHERE department_id = 1
AND salary > 70000;

-- Check sorting performance
EXPLAIN ANALYZE
SELECT *
FROM employees
ORDER BY salary DESC;

-- Check JOIN query performance
EXPLAIN ANALYZE
SELECT
    e.employee_name,
    d.department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id
WHERE e.department_id = 1;

-- Check all indexes on employees
SELECT
    indexname,
    indexdef
FROM pg_indexes
WHERE tablename = 'employees';

-- Understand PRIMARY KEY index
-- PostgreSQL automatically creates an index for a PRIMARY KEY
SELECT
    indexname,
    indexdef
FROM pg_indexes
WHERE tablename = 'employees';

-- Final performance practice
-- Find IT employees earning more than 75000
EXPLAIN ANALYZE
SELECT
    e.employee_name,
    e.salary,
    d.department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id
WHERE e.department_id = 1
AND e.salary > 75000;

-- Remove an index
-- DROP INDEX IF EXISTS idx_employees_name;

-- Rebuild an existing index
-- REINDEX INDEX idx_department_salary;