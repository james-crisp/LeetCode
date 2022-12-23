# James Crisp
# Dec 23, 2022

# 1873. Calculate Special Bonus

# Write your MySQL query statement below

SELECT employee_id, CASE
    WHEN employee_id % 2 = 0 or SUBSTRING(name,1,1) = 'M'
        THEN 0
        ELSE salary
    END as bonus
FROM Employees
ORDER BY employee_id ASC