# Write your MySQL query statement below
WITH CTE AS (
    SELECT e.id as emp_id,e.name as Employee,
        d.id as dept_id, d.name as Department,
        e.salary as Salary,
        DENSE_RANK() OVER (PARTITION BY d.name ORDER BY e.salary DESC) AS value
    FROM Employee e
    JOIN Department d
        ON e.departmentId = d.id
)

SELECT Employee, Department, Salary
FROM CTE
WHERE value <= 3