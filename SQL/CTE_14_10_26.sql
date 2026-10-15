show databases;
use firstwork;
show tables;
-- section A — 10 Normal / Single CTE Questions
-- 1. Find all employees whose salary is greater than 60,000 using a single CTE.
with cte1 as(select * from employee_details where salary>60000) select * from cte1;
#2. Find the employee(s) who earn the highest salary using a single CTE.
with cte1 as(select max(salary) from employee_details) select * from cte1;
#3. Find the employee(s) who earn the lowest salary using a single CTE.
with cte1 as(select min(salary) from employee_details) select * from cte1;
#4. Find employees whose salary is greater than the average salary using a single CTE.
with cte1 as(select * from employee_details where salary>(select avg(salary) from employee_details)) select * from cte1;
#5. Find employees whose salary is less than the average salary using a single CTE.
with cte1 as(select * from employee_details where salary<(select avg(salary) from employee_details)) select * from cte1;
#6. Find the total salary paid by the company using a single CTE.
with cte1 as(select sum(salary) from employee_details) select * from cte1;
#7. Find the average salary of employees using a single CTE and display the result with a meaningful column name.
with cte1 as(select avg(salary) as Average_Salary from employee_details) select * from cte1;
#8. Find the employees working in the IT department using a single CTE.
with cte1 as(select * from employee_details where department='IT') select * from cte1;
#9. Find the number of employees in the company using a single CTE.
with cte1 as(select count(emp_id) from employee_details) select * from cte1;
#10. Find the employees who have more than 25 using a single CTE.
with cte1 as(select * from employee_details where age>25) select * from cte1;
-- Section B — Multiple CTE Questions
-- 1. Create one CTE to calculate the average salary and another CTE to find employees earning more than the average salary.
with cte1 as(select avg(salary) from employee_details) ,cte2 as (select * from employee_details where salary>(select * from cte1)) select * from cte2;
#2. Create one CTE to find the maximum salary and another CTE to find all employees earning that maximum salary.
with cte1 as (select max(salary) from employee_details),cte2 as (select * from employee_details where salary=(select * from cte1))select * from cte2;
#4. Create one CTE to filter employees with above 25 age and another CTE to find the average salary of those employees.
with cte1 as(select * from employee_details where age>25),cte2 as (select avg(salary) from cte1) select * from cte2;
#5. Create one CTE to calculate total salary by department and another CTE to find departments whose total salary is greater than 150,000.
with cte1 as(select department,sum(salary) as Total_Salary from employee_details group by department),cte2 as(select * from cte1 where Total_Salary>150000)select * from cte2;
#6. Create one CTE to find employees in the IT department and another CTE to find the highest-paid employee among those IT employees.
with cte1 as(select * from employee_details where department='IT'),cte2 as (select * from cte1 where salary=(select max(salary) from cte1 ))select * from cte2;
#7. Create one CTE to find employees earning more than 60,000 and another CTE to count how many such employees exist in each department.
with cte1 as(select emp_name as Highest from employee_details where salary>60000),cte2 as (select count(Highest) from cte1)select * from cte2;
#8. Create one CTE to calculate the average salary by department and another CTE to find departments whose average salary is greater than the company's overall average salary.
with cte1 as(select department,avg(salary) as Average from employee_details group by department),cte2 as(select department from cte1 where Average>(select avg(salary) from employee_details)) select * from cte2;