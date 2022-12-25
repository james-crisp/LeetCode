# James Crisp
# Dec 25, 2022

# 1667. Fix Names in a Table

# Write your MySQL query statement below

SELECT user_id, UPPER(LEFT(name,1))+LOWER(SUBSTRING(name,2,LEN(name)))
FROM Users;
