create database  analytics_demo;

USE analytics_demo;

CREATE TABLE customers (
  customer_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  city VARCHAR(50)
);

CREATE TABLE orders (
  order_id INT PRIMARY KEY AUTO_INCREMENT,
  customer_id INT,
  product VARCHAR(50),
  amount DECIMAL(10,2),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

INSERT INTO customers (name, city) VALUES
('Rohan', 'Mumbai'),
('Priya', 'Delhi'),
('Karan', 'Pune'),
('Neha', 'Chennai');

INSERT INTO orders (customer_id, product, amount) VALUES
(1, 'Laptop', 50000),
(3, 'Mobile', 20000),
(1, 'Mouse', 1500),
(5, 'Headphones', 3000);

SELECT c.name, c.city, o.product, o.amount
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;

create database company; 

use company;

-- Create two tables: employees and departments.
create table employees ( 
 employee_id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50),
  city VARCHAR(50)
);

create table departments (
	dept_id int primary key auto_increment,
	dept_name varchar(50),
	city varchar(50)
);

-- Insert sample data for 4 employees and 2 departments.
insert into employees (name,city) values
("Raj", "Mumbai"),
("Rohan", "Delhi"),
("Mohan", "Kolkata"),
("Het", "Banglore");

insert into departments (dept_name,city) values
("IT", "chennai"),
("Finance", "ahmedabad");

-- Write a query using INNER JOIN to list employee names with their department names.
SELECT employees.name, departments.dept_name
FROM employees
INNER JOIN departments
ON employees.city = departments.city;