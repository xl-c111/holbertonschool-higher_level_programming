-- List all shows without a genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.show_id is NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;


-- LEFT JOIN remains all shows 
-- WHERE ... is NULL filters to keep only shows with no matching genres