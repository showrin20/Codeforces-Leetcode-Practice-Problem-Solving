# Write your MySQL query statement below
select EmployeeUNI.unique_id,Employees.name 
from Employees
Left join EmployeeUNI On EmployeeUNI.Id = Employees.Id
