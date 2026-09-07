show databases;
use firstwork;
show tables;
select * from employee_details;
#1. Display the number of employees in each department.
select department,count(emp_name) from employee_details group by department;
#2. Find the total salary paid by each department.
select department,sum(salary) from employee_details group by department;
#3. Find the average salary of each department.
select department,avg(salary) from employee_details group by department;
#4. Display the highest salary in each department.
select department,max(salary) from employee_details group by department;
#5. Display the lowest salary in each department.
select department,min(salary) from employee_details group by department;
#6. Find the salary difference (MAX - MIN) for each department.
select department,max(salary)-min(salary) from employee_details group by department;
#7. Display the total number of departments.
select department,count(distinct department) from employee_details group by department;
#8. Find the total salary and average salary for each department.
select department,sum(department),avg(department) from employee_details group by department;
#9. Display each department along with its employee count and total salary.
select department,count(emp_id),sum(salary) from employee_details group by department;
#10. Sort the departments based on their average salary in descending order.
select department, avg(salary) from employee_details group by department  order by avg(salary) desc;
### HAVING Questions

#11. Display departments having more than 2 employees.
select department from employee_details group by department having count(emp_id)>2;
#12. Display departments whose average salary is greater than 60,000.
select department from employee_details group by department having avg(salary)>60000;
# 13 Display departments whose total salary is greater than 1,80,000.
select department from employee_details group by department having sum(salary)>180000;
#14. Display departments whose maximum salary is greater than 70,000.
select department from employee_details group by department having max(salary)>70000;
#15. Display departments whose minimum salary is less than 50,000.
select department from employee_details group by department having min(salary)<50000;
#16. Display departments having exactly 3 employees.
select department from employee_details group by department having count(emp_id)=3;
#17. Display departments having fewer than 3 employees.
select department from employee_details group by department having count(emp_id)<3;
#18. Display departments whose average salary is between 50,000 and 70,000.
select department from employee_details group by department having avg(salary) between 50000 and 70000;
#19. Display departments whose total salary is less than 1,50,000.
select department from employee_details group by department having sum(salary)<150000;
#20. Display departments where the highest salary is at least 80,000.
select department from employee_details group by department having max(salary)>=80000;








