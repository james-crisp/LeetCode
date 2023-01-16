# James Crisp
# Jan 16, 2023

# 178. Rank Scores

# Write your MySQL query statement below

SELECT  score,
        RANK() OVER(PARTITION BY score ORDER BY score DESC) rank
FROM Scores
ORDER BY score DESC;