# James Crisp
# Dec 19, 2022

# 595. Big Countries 


# Write your MySQL query statement below

SELECT name, population, area
FROM World
WHERE population >= 25000000 or area > 3000000;