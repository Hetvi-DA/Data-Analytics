create database companydb;

use companydb;

create table employee(
	employee_id int primary key,
    employee_name varchar(50),
    employee_salary int,
    employee_age int,
    employee_dpt varchar(50)
);

insert into employee values
(1,"Rohan",50000,24,"Sales"),
(2,"Mohan",45000,26,"HR"),
(3,"Raj",30000,28,"Finance"),
(4,"Alex",25000,30,"Marketing"),
(5,"Rohit",40000,25,"IT");

select * from employee
limit 2 ;

select * from employee
order by employee_salary asc;

select * from employee
order by employee_salary desc;

select * from employee
where employee_name like '%A%' ;

select * from employee
where employee_dpt in ("sales","IT","HR");

select * from employee
where employee_salary between 30000 and 45000;

select * from employee
where not employee_dpt="Sales";

select * from employee
where employee_dpt="Sales" or employee_dpt="IT";

select * from employee
where employee_dpt="Sales" and employee_salary>45000;

select * from employee
where employee_salary>30000;

select * from employee
where employee_age>25;
