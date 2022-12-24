# James Crisp
# Dec 24, 2022

# 627. Swap Salary

# Write your MySQL query statement below

UPDATE Salary
SET sex = CASE
        WHEN sex = 'm' THEN 'f'
        WHEN sex = 'f' THEN 'm'
    END
    