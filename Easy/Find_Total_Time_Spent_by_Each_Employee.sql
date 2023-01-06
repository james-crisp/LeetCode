# James Crisp
# Jan 6, 2023

# 1741. Find Total Time Spent by Each Employee

# Write your MySQL query statement below

SELECT event_day as day, emp_id, SUM(out_time-in_time) as total_time
FROM Employees
GROUP BY day,emp_id;