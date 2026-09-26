# Write your MySQL query statement below
SELECT *, 
    CASE 
        WHEN 
            x+y>z AND abs(x-y) < z
            AND y+z > x AND abs(y-z) < x 
            AND z+x > y AND abs(z-x) < y
        THEN "Yes"
        ELSE "No"
    END AS triangle
FROM Triangle