-- DAY 4: POSTGRESQL / SQL
-- Employee Management Practice


-- 1. Check PostgreSQL version
SELECT version();


-- 2. Create schema
CREATE SCHEMA IF NOT EXISTS company;


-- 3. Create departments table
CREATE TABLE IF NOT EXISTS company.departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);


-- 4. Create employees table
CREATE TABLE IF NOT EXISTS company.employees (
    employee_id SERIAL PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE,
    department_id INT,
    salary NUMERIC(10,2),
    city VARCHAR(50),
    joining_date DATE,
    is_active BOOLEAN DEFAULT TRUE,
    
    FOREIGN KEY (department_id)
    REFERENCES company.departments(department_id)
);


-- 5. Insert departments
INSERT INTO company.departments (department_name)
VALUES
('IT'),
('HR'),
('Finance'),
('Marketing');


-- 6. Insert employees
INSERT INTO company.employees
(employee_name, email, department_id, salary, city, joining_date)
VALUES
('Amit', 'amit@gmail.com', 1, 75000, 'Pune', '2022-06-10'),
('Priya', 'priya@gmail.com', 2, 60000, 'Mumbai', '2023-01-15'),
('Rahul', 'rahul@gmail.com', 1, 85000, 'Pune', '2021-08-20'),
('Sneha', 'sneha@gmail.com', 3, 70000, 'Kolhapur', '2024-02-12'),
('Neha', 'neha@gmail.com', 1, 90000, 'Mumbai', '2020-11-05'),
('Kiran', 'kiran@gmail.com', 4, 65000, 'Pune', '2023-07-18'),
('Rohit', 'rohit@gmail.com', 3, 80000, 'Mumbai', '2022-03-25'),
('Pooja', 'pooja@gmail.com', 2, 62000, 'Kolhapur', '2024-06-01');

-- 7. Display all employees
SELECT * FROM company.employees;


-- 8. Select specific columns
SELECT employee_name, salary, city
FROM company.employees;


-- 9. WHERE
SELECT * FROM company.employees
WHERE salary > 70000;


-- 10. AND
SELECT * FROM company.employees
WHERE salary > 70000
AND city = 'Pune';


-- 11. OR
SELECT * FROM company.employees
WHERE city = 'Pune'
OR city = 'Mumbai';


-- 12. BETWEEN
SELECT * FROM company.employees
WHERE salary BETWEEN 60000 AND 80000;


-- 13. IN
SELECT * FROM company.employees
WHERE city IN ('Pune', 'Mumbai');


-- 14. LIKE
SELECT * FROM company.employees
WHERE employee_name LIKE 'P%';


-- 15. PostgreSQL ILIKE
SELECT * FROM company.employees
WHERE employee_name ILIKE 'p%';


-- 16. ORDER BY
SELECT * FROM company.employees
ORDER BY salary DESC;


-- 17. LIMIT
SELECT * FROM company.employees
ORDER BY salary DESC
LIMIT 3;


-- 18. DISTINCT
SELECT DISTINCT city
FROM company.employees;


-- 19. COUNT
SELECT COUNT(*) AS total_employees
FROM company.employees;


-- 20. Aggregate functions
SELECT
    COUNT(*) AS total_employees,
    SUM(salary) AS total_salary,
    AVG(salary) AS average_salary,
    MIN(salary) AS minimum_salary,
    MAX(salary) AS maximum_salary
FROM company.employees;


-- 21. GROUP BY
SELECT department_id, COUNT(*) AS employee_count
FROM company.employees
GROUP BY department_id;


-- 22. GROUP BY with average salary
SELECT department_id, AVG(salary) AS average_salary
FROM company.employees
GROUP BY department_id;


-- 23. HAVING
SELECT department_id, AVG(salary) AS average_salary
FROM company.employees
GROUP BY department_id
HAVING AVG(salary) > 70000;


-- 24. UPDATE
UPDATE company.employees
SET salary = 78000
WHERE employee_id = 1;


-- 25. Check updated record
SELECT * FROM company.employees
WHERE employee_id = 1;


-- 26. DELETE one record
DELETE FROM company.employees
WHERE employee_id = 8;


-- 27. Check remaining employees
SELECT * FROM company.employees;


-- 28. Basic INNER JOIN
SELECT e.employee_name, d.department_name, e.salary
FROM company.employees e
INNER JOIN company.departments d
ON e.department_id = d.department_id;


-- 29. Basic LEFT JOIN
SELECT e.employee_name, d.department_name
FROM company.employees e
LEFT JOIN company.departments d
ON e.department_id = d.department_id;


-- 30. JOIN with condition
SELECT e.employee_name, d.department_name, e.salary
FROM company.employees e
JOIN company.departments d
ON e.department_id = d.department_id
WHERE e.salary > 70000;