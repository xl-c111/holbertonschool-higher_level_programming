-- List all shows, and all genres linked to that show
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;



-- Workflow
-- 1, Start from the maim table tv_shows, list all shows 
-- 2, Use tv_show_genres to link shows to genres
-- 3, Use LEFT JOIN to include shows without genres
-- 4, Select Column to display: show title, genre name