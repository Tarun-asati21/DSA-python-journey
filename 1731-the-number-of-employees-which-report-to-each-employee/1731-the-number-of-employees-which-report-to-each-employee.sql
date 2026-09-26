# Write your MySQL query statement below
WITH temp AS (
    SELECT reports_to, COUNT(employee_id) AS reports_count, ROUND(AVG(age)) AS average_age
    FROM Employees
    WHERE reports_to IS NOT NULL 
    GROUP BY reports_to
    HAVING reports_count >= 1
)
SELECT e.employee_id, e.name, t.reports_count, t.average_age
FROM Employees e
JOIN temp t
    ON e.employee_id = t.reports_to
ORDER BY employee_id

