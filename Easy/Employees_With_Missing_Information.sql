# James Crisp
# Jan 1, 2023

# 1965. Employees With Missing Information

# Write your MySQL query statement below

SELECT employee_id
FROM Employees
INNER JOIN Salaries ON Employees.employee_id=Salaries.employee_id;