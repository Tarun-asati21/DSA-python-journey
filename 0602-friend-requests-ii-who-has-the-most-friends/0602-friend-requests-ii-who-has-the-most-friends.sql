# Write your MySQL query statement below
WITH CTE1 AS (
    SELECT requester_id AS id
    FROM RequestAccepted
), 
CTE2 AS(
    SELECT accepter_id AS id 
    FROM RequestAccepted
),
CTE3 AS(
    SELECT *
    FROM CTE1

    UNION ALL

    SELECT *
    FROM CTE2
)

SELECT id, COUNT(id) as num
FROM CTE3
GROUP BY id
ORDER BY num DESC
LIMIT 1