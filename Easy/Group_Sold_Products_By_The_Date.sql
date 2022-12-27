# James Crisp
# Dec 27, 2022

# 1484. Group Sold Products By The Date

# Write your MySQL query statement below

SELECT sell_date, COUNT(DISTINCT product) as num_sold, GROUP_CONCAT(DISTINCT product order by product ASC) as products
FROM Activities
GROUP BY sell_date;