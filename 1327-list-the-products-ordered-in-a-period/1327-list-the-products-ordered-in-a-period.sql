# Write your MySQL query statement below
WITH CTE AS(
    SELECT p.product_id, p.product_name, YEAR(o.order_date) AS order_year, MONTH(o.order_date) AS order_month, o.unit
    FROM Products p
    JOIN Orders o
        ON p.product_id = o.product_id
)
SELECT product_name, SUM(unit) AS unit
FROM CTE
WHERE order_year = 2020
    AND order_month = 2
GROUP BY product_name
HAVING unit >= 100;