# James Crisp

# 181. Employees Earning More Than Their Managers

# Write your MySQL query statement below

SELECT Person1.name as Employee
FROM Employee as Person1, Employee as Person2
WHERE Person1.managerId = Person2.Id and Person1.salary > Person2.salary;