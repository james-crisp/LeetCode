# James Crisp

# 586. Customer Placing the Largest Number of Orders

# Write your MySQL query statement below

SELECT MAX (mycount) FROM (COUNT(customer_number) as mycount FROM Orders GROUP BY customer_number);
