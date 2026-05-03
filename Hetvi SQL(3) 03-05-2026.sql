create database studentdb;

use studentdb;

-- Step 1: Create Table
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  course VARCHAR(30),
  marks INT
);

-- Step 2: Insert Sample Data
INSERT INTO students (id, name, course, marks) VALUES
(1, 'Aman', 'BCA', 78),
(2, 'Neha', 'MCA', 90),
(3, 'Riya', 'BBA', 62),
(4, 'Karan', 'BCA', 55),
(5, 'Meena', 'MCA', 88);

-- Step 3: Filter Students with Marks > 70
SELECT * 
FROM students
WHERE marks > 70;

-- Sort Students by Marks in Descending Order
SELECT name, course, marks
FROM students
ORDER BY marks DESC;

-- Display Only BCA Students, Sorted by Marks (Lowest to Highest)
SELECT name, marks
from students
where course ='BCA'
order by marks asc;

-- Update Marks of a Specific Student

 SET SQL_SAFE_UPDATES = 0;
 
 UPDATE students
SET marks = 95
WHERE name = 'Neha';

-- Verify Update
SELECT * FROM students WHERE name = 'Neha';

SET SQL_SAFE_UPDATES = 1;

-- Delete a Student Record
DELETE FROM students
WHERE id = 4;

-- Verify Deletion
SELECT * FROM students;

Display all students who have marks greater than 70.
select * from students
where marks > 70;

Show names and course of students enrolled in BCA.
select  name,course from students
where course ="BCA";

Display all students whose names start with the letter ‘A’
select * from students
where name like 'A%';

List students whose marks are between 60 and 90.
select * from students
where marks between 60 and 90;

Show all students except those in the BBA course.
select * from students
where not course ="BBA";

Display student names and marks, sorted by marks in descending order.
select name , marks from students
order by marks desc;

Display all students whose course name ends with “A”.
select * from students
where course like '%A';

Update marks of a student named ‘Riya’ to 85.
SET SQL_SAFE_UPDATES = 0;

update students
set marks = 85
where name = 'riya';

SET SQL_SAFE_UPDATES = 1;

Delete the student record whose id = 5.
delete from students
where id = 5;

Show all students with marks greater than 60 and order them by name (A–Z).
select marks, name from students
where marks > 60
order by name asc;



