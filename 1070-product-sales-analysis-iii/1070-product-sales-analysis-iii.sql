# Write your MySQL query statement below
WITH temporary AS(
    SELECT product_id,
        MIN(year) as first_year
    FROM Sales
    GROUP BY product_id
)
SELECT 
    p.product_id, 
    t.first_year,
    p.quantity, 
    p.price
FROM Sales p
JOIN temporary t
    ON p.year = t.first_year
    AND p.product_id = t.product_id
