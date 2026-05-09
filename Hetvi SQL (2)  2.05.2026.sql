create database empDB;

use empDB;

CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  course VARCHAR(20),
  marks INT
);

INSERT INTO students VALUES
(1, 'Aman', 'BCA', 75),
(2, 'Neha', 'MCA', 90),
(3, 'Karan', 'BCA', 65),
(4, 'Riya', 'BBA', 80),
(5, 'Meena', 'MCA', 88);

select course , AVG(marks) as average_marks
from students
group by course;

SELECT course, AVG(marks) AS avg_marks
FROM students
GROUP BY course
HAVING AVG(marks) > 70;

select name, marks
from students
order by marks desc
limit 3;

SELECT * FROM students
WHERE course IN ('BCA', 'MCA')
AND marks BETWEEN 70 AND 90;

SELECT
	COUNT(*) AS total_students,
    SUM(marks) AS total_marks,
    AVG(marks) AS average_marks,
    MAX(marks) AS highest_marks,
    MIN(marks) AS lowest_marks
FROM students;

Count the total number of students in the table.
select
	COUNT(*) AS total_students FROM students;
    
 Display the highest and lowest marks.   
  SELECT
	MAX(marks) AS highest_marks ,
    MIN(marks) AS lowest_marks 
FROM students;

Show total marks obtained by students in each course.
SELECT 
	SUM(marks) AS total_marks
    FROM students
    GROUP BY course;

Display the average marks per course using GROUP BY.
SELECT
	AVG(marks) AS average_marks
    FROM students
    GROUP BY course;
    
Show only those courses whose average marks exceed 80 using HAVING.
    SELECT
		AVG(marks) AS average_marks
        FROM students
        GROUP BY course
        HAVING AVG(marks) > 80;
        
        Display the top 2 scoring students using ORDER BY and LIMIT.
        SELECT marks
			FROM students
            ORDER BY marks DESC
            LIMIT 2;
            
Show all students whose marks are between 60 and 90.
SELECT marks
	FROM students
    where marks between 60 and 90;
            
Display all students enrolled in BCA or MCA using IN.
SELECT * FROM students
WHERE course IN ("BCA","MCA");

Find the total number of unique courses (COUNT(DISTINCT course)).
SELECT
	COUNT(DISTINCT course) AS distinct_course
FROM students;

Display names of students whose names start with ‘N’ using LIKE.
SELECT * FROM students
WHERE name LIKE 'N%';

