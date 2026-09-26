# Write your MySQL query statement below
WITH CTE AS (
    SELECT *
    FROM Activities
    ORDER BY product
)
SELECT sell_date, 
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(DISTINCT product SEPARATOR ",") AS products
FROM CTE
GROUP BY sell_date