# James Crisp
# Jan 16, 2023

# 178. Rank Scores

/* Write your T-SQL query statement below */

SELECT  score,
        DENSE_RANK() OVER(ORDER BY score DESC) Rank
FROM Scores
ORDER BY Rank;