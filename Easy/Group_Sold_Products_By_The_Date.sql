# James Crisp
# Dec 27, 2022

# 1484. Group Sold Products By The Date

# Write your MySQL query statement below

SELECT sell_date, COUNT(*) as num_sold
FROM Activities
GROUP BY sell_date;