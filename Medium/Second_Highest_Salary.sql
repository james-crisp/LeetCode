# James Crisp
# Jan 15, 2023

# 176. Second Highest Salary

# Write your MySQL query statement below

SELECT MAX(salary) AS SecondHighestSalary FROM Employee WHERE salary NOT IN (SELECT MAX(salary) FROM Employee);
