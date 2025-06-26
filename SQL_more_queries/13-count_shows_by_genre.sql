-- List all genres and display the number of shows linked to each
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC;


-- GROUP BY(tv_genres.id): group rows by genre id, put same values together
-- COUNT(column): count how many shows in each group(skip empty/null ones)
