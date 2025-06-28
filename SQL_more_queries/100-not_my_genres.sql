-- List all genres not linked to the show Dexter
SELECT DISTINCT tv_genres.name
FROM tv_genres
WHERE tv_genres.id NOT IN(
    SELECT genre_id
    FROM tv_show_genres
    JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name ASC;




-- Workflow
-- 1, Subquery: Using tv_show_genres and tv_shows to find all genre IDs linked to 'Dexter'
-- 2, In the genre table, excludes all these IDs
--    Syntax: WHERE ...NOT IN()
-- 3, Keep the remaining genres 
-- 4, Sort the final result by genre name