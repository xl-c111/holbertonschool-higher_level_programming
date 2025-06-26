-- List all genres and display the number of shows linked to each
SELECT tv_genres.name, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.show_id
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC;

-- COUNT(column): count how many in each group(skip empty/null ones)
-- GROUP BY: group by category, put same values together