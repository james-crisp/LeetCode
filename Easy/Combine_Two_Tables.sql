# James Crisp
# Dec 29, 2022

# 175. Combine Two Tables

# Write your MySQL query statement below

SELECT firstName, lastName, city, state
FROM Person
LEFT OUTER JOIN Address ON Address.personID=Person.personID;
