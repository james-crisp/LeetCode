# James Crisp
# Dec 25, 2022

# 1667. Fix Names in a Table

# Write your MySQL query statement below

SELECT user_id, CONCAT(UPPER(LEFT(name,1)),LOWER(SUBSTRING(name,2))) as name
FROM Users
ORDER BY user_id;
