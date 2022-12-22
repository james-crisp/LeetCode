# James Crisp
# Dec 21, 2022

# 584. Find Customer Referee

# Write your MySQL query statement below

SELECT name
FROM Customer
WHERE referee_id != 2 or referee_id IS NULL;