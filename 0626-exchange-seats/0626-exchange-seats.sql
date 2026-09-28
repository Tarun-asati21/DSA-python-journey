# Write your MySQL query statement below
# my solution 
-- WITH temp AS (
--     SELECT *
--     FROM Seat
--     ORDER BY id DESC
--     LIMIT 1 
-- )

-- SELECT s1.id , s2.student
-- FROM Seat s1
-- JOIN Seat s2
--     ON s1.id%2=0 AND s1.id - 1 = s2.id

-- UNION ALL

-- SELECT s1.id , s2.student
-- FROM Seat s1
-- JOIN Seat s2
--     ON s1.id%2!=0 AND s1.id + 1 = s2.id

-- UNION ALL

-- SELECT id, student
-- FROM temp
-- WHERE id%2!=0

-- ORDER BY id;

# neat and clean query 
# Write your MySQL query statement below
select case when id % 2 =1 and id+1 in (select id from Seat) then id+1
            when id % 2 =0 then id-1
            else id
        end as id, student
        from Seat
        order by id;