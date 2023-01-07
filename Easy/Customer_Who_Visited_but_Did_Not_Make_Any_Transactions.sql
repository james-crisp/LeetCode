# James Crisp
# Jan 7, 2023

# 1581. Customer Who Visited but Did Not Make Any Transactions

# Write your MySQL query statement below

SELECT customer_id
FROM Visits
LEFT JOIN Transactions ON Visits.visit_id=Transactions.visit_id;