# Write your MySQL query statement below
WITH temp AS (
    SELECT num,
        LEAD(num,1) OVER() AS num1,
        LEAD(num,2) OVER() AS num2
    FROM Logs
)
SELECT DISTINCT num as ConsecutiveNums
FROM temp
WHERE num = num1 
    AND num = num2