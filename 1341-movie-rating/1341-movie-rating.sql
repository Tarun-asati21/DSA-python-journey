# Write your MySQL query statement below
WITH temp1 AS (
    SELECT m.user_id, u.name, COUNT(movie_id) AS total_rated
    FROM MovieRating m
    JOIN Users u
        ON u.user_id = m.user_id
    GROUP BY user_id
    ORDER BY total_rated DESC, name ASC
    LIMIT 1
),
temp2 AS (
    SELECT m.title, r.movie_id, r.rating,
        MONTH(r.created_at) AS review_month, YEAR(r.created_at) AS review_year
    FROM MovieRating r
    JOIN Movies m
        ON m.movie_id = r.movie_id
),
temp3 AS (
    SELECT title, AVG(rating) AS average
    FROM temp2
    WHERE review_month = 2
        AND review_year = 2020
    GROUP BY title
    ORDER BY average DESC, title ASC
    LIMIT 1
)

SELECT name as results
FROM temp1

UNION ALL

SELECT title as results
FROM temp3