# James Crisp
# Dec 20, 2022

# Problem 1757. Recyclable and Low Fat Products

# Write your MySQL query statement below

SELECT product_id
FROM Products
WHERE low_fats = 'Y' and recyclable = 'Y';