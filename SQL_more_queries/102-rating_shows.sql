-- List all shows from hbtn_0d_tvshows_rate by their rating
SELECT tv_shows.title, SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
-- group the result by each show ID
GROUP BY tv_shows.id
ORDER BY rating DESC;



-- Workflow - get sum of ratings per show
-- 1, tv_show_ratings holds score, tv_shows holds title
-- 2, JOIN both tables by show_id
-- 3, Use GROUP BY tv_shows.id to group all ratings for the same show together
-- 4, Use SUM(rate) to get total rating per group 
