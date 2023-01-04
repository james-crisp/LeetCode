# James Crisp
# Jan 1, 2023

# 1965. Employees With Missing Information

# Write your MySQL query statement below
SELECT T.employee_id
FROM
    (SELECT employee_id FROM Employees
    UNION
    SELECT employee_id FROM Salaries)
AS T
WHERE T.salary IS NULL or T.name IS NULL;



