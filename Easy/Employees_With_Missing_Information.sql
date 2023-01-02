# James Crisp
# Jan 1, 2023

# 1965. Employees With Missing Information

# Write your MySQL query statement below

# Write your MySQL query statement below

SELECT
    CASE WHEN Employees.employee_id != Salaries.employee_id
        THEN Employees.employee_id
    END
    AS employee_id
FROM Employees
LEFT JOIN Salaries ON Employees.employee_id=Salaries.employee_id;
