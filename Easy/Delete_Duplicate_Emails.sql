# James Crisp
# Dec 24, 2022

# 196. Delete Duplicate Emails

# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below

DELETE p1 from Person p1, Person p2
WHERE p1.email = p2.email and p1.id > p2.id