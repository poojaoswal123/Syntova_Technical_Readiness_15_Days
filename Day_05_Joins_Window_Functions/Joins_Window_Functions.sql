-- DAY 5: JOINS & WINDOW FUNCTIONS
-- PostgreSQL Practice

-- 1. Create departments table
CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

-- 2. Create employees table
-- manager_id is used later for SELF JOIN
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    department_id INT,
    salary NUMERIC(10,2),
    city VARCHAR(50),
    manager_id INT
);

-- 3. Create projects table
CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    department_id INT
);

-- 4. Insert departments
INSERT INTO departments
(department_id, department_name)
VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Finance'),
(4, 'Marketing');

-- 5. Insert employees
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

-- 6. Insert projects
INSERT INTO projects
(project_id, project_name, department_id)
VALUES
(1, 'AI Project', 1),
(2, 'Recruitment System', 2),
(3, 'Finance Dashboard', 3),
(4, 'Marketing Website', 4);

-- 7. View all tables
SELECT * FROM departments;
SELECT * FROM employees;
SELECT * FROM projects;

-- 8. INNER JOIN
-- Shows only employees who have a matching department
SELECT e.employee_name, d.department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id;

-- 9. LEFT JOIN
-- Shows all employees and their department if available
SELECT e.employee_name, d.department_name
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id;

-- 10. RIGHT JOIN
-- Shows all departments and matching employees
SELECT e.employee_name, d.department_name
FROM employees e
RIGHT JOIN departments d
ON e.department_id = d.department_id;

-- 11. FULL OUTER JOIN
-- Shows all employees and all departments
SELECT e.employee_name, d.department_name
FROM employees e
FULL OUTER JOIN departments d
ON e.department_id = d.department_id;

-- 12. CROSS JOIN
-- Creates every possible employee-department combination
SELECT e.employee_name, d.department_name
FROM employees e
CROSS JOIN departments d;

-- 13. SELF JOIN
-- Joins employees table with itself to find employee and manager
SELECT e.employee_name AS employee, m.employee_name AS manager
FROM employees e
LEFT JOIN employees m
ON e.manager_id = m.employee_id;

-- 14. JOIN with WHERE
-- Shows employees whose salary is greater than 70000
SELECT e.employee_name, d.department_name, e.salary
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id
WHERE e.salary > 70000;

-- 15. JOIN with ORDER BY
-- Shows employees from highest to lowest salary
SELECT e.employee_name, d.department_name, e.salary
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id
ORDER BY e.salary DESC;

-- 16. JOIN with GROUP BY
-- Counts employees in each department
SELECT d.department_name, COUNT(e.employee_id) AS employee_count
FROM departments d
LEFT JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_name;

-- 17. Multiple-table JOIN
-- Joins employees, departments and projects
SELECT e.employee_name, d.department_name, p.project_name, e.salary
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id
INNER JOIN projects p
ON d.department_id = p.department_id;

-- 18. Multiple-table JOIN with WHERE
-- Shows IT employees and their project
SELECT e.employee_name, d.department_name, p.project_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id
INNER JOIN projects p
ON d.department_id = p.department_id
WHERE d.department_name = 'IT';

-- 19. OVER()
-- Applies a window function to all rows
SELECT employee_name, salary,
AVG(salary) OVER() AS overall_average_salary
FROM employees;

-- 20. ROW_NUMBER()
-- Gives a unique number to each employee based on salary
SELECT employee_name, salary,
ROW_NUMBER() OVER(ORDER BY salary DESC) AS row_number
FROM employees;

-- 21. RANK()
-- Gives the same rank when salaries are equal
SELECT employee_name, salary,
RANK() OVER(ORDER BY salary DESC) AS salary_rank
FROM employees;

-- 22. DENSE_RANK()
-- Similar to RANK but does not skip rank numbers
SELECT employee_name, salary,
DENSE_RANK() OVER(ORDER BY salary DESC) AS salary_rank
FROM employees;

-- 23. ROW_NUMBER() with PARTITION BY
-- Numbers employees separately inside each department
SELECT employee_name, department_id, salary,
ROW_NUMBER() OVER(PARTITION BY department_id ORDER BY salary DESC) AS department_row_number
FROM employees;

-- 24. RANK() with PARTITION BY
-- Ranks employees separately inside each department
SELECT employee_name, department_id, salary,
RANK() OVER(PARTITION BY department_id ORDER BY salary DESC) AS department_rank
FROM employees;

-- 25. DENSE_RANK() with PARTITION BY
-- Gives dense salary ranking inside each department
SELECT employee_name, department_id, salary, 
DENSE_RANK() OVER(PARTITION BY department_id ORDER BY salary DESC) AS department_rank
FROM employees;

-- 26. COUNT() OVER()
-- Shows total employee count on every row
SELECT employee_name, department_id,
COUNT(*) OVER() AS total_employees
FROM employees;

-- 27. COUNT() OVER(PARTITION BY)
-- Shows employee count for each employee's department
SELECT employee_name, department_id,
COUNT(*) OVER(PARTITION BY department_id) AS department_employee_count
FROM employees;

-- 28. AVG() OVER(PARTITION BY)
-- Shows department average salary for every employee
SELECT employee_name, department_id,salary,
AVG(salary) OVER(PARTITION BY department_id) AS department_average_salary
FROM employees;

-- 29. JOIN + Window Function
-- Shows employee, department and salary rank
SELECT e.employee_name, d.department_name, e.salary,
RANK() OVER(PARTITION BY e.department_id ORDER BY e.salary DESC) AS department_salary_rank
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id;

-- 30. LAG()
-- Gives you previous row
SELECT employee_name, salary,
LAG(salary) OVER(ORDER BY salary DESC) AS previous_salary
FROM employees;

-- 31. LEAD()
-- Give you next row
SELECT employee_name, salary,
LEAD(salary) OVER(ORDER BY salary DESC) AS next_salary
FROM employees;