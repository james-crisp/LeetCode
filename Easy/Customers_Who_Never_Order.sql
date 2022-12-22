# James Crisp
# December 22, 2022

# 183. Customers Who Never Order

# Write your MySQL query statement below

SELECT name as Customers
FROM Customers
WHERE id NOT IN (SELECT customerID FROM Orders);