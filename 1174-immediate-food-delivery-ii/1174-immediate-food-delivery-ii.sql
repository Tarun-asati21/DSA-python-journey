# Write your MySQL query statement below
-- use of CTE (common table expression)
WITH temporary AS (
    SELECT 
        customer_id, 
        MIN(order_date) AS first_order_date
    FROM Delivery
    GROUP BY customer_id
)
SELECT 
    ROUND(
        AVG(
            CASE 
                WHEN t.first_order_date = d.customer_pref_delivery_date THEN 100
                ELSE 0
            END
        ), 2) AS immediate_percentage
FROM temporary t
JOIN Delivery d
    ON t.first_order_date = d.order_date
    AND t.customer_id = d.customer_id
