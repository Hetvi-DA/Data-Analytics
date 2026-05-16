CREATE DATABASE companydb2;

USE companydb2;

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT,
    salary INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
-- Insert sample data for 4 employees and 2 departments.
INSERT INTO departments VALUES
(1, 'HR'),
(2, 'IT');

INSERT INTO employees VALUES
(101, 'Amit', 1, 40000),
(102, 'Priya', 2, 50000),
(103, 'Rahul', 2, 45000),
(104, 'Sneha', NULL, 35000);

-- Write a query using INNER JOIN to list employee names with their department names.
SELECT 
    e.emp_name,
    d.dept_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id;

-- Write a LEFT JOIN to show all departments, even if they have no employees.
SELECT 
    d.dept_name,
    e.emp_name
FROM departments d
left JOIN employees e
ON d.dept_id = e.dept_id;

-- Write a RIGHT JOIN to show all employees, even if their department ID is missing.
SELECT 
    e.emp_name,
    d.dept_name
FROM departments d
RIGHT JOIN employees e
ON d.dept_id = e.dept_id;

-- Simulate a FULL JOIN between both tables using UNION.
SELECT 
    e.emp_name,
    d.dept_name
FROM employees e
LEFT JOIN departments d
ON e.dept_id = d.dept_id

UNION

SELECT 
    e.emp_name,
    d.dept_name
FROM employees e
RIGHT JOIN departments d
ON e.dept_id = d.dept_id;

-- Create a third table projects and perform a multi-table JOIN among all three tables.
CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(50),
    emp_id INT,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);

INSERT INTO projects VALUES
(201, 'Website Development', 102),
(202, 'HR Management System', 101),
(203, 'Mobile App', 103);

SELECT 
    e.emp_name, d.dept_name, p.project_name
FROM
    employees e
        INNER JOIN
    departments d ON e.dept_id = d.dept_id
        INNER JOIN
    projects p ON e.emp_id = p.emp_id;