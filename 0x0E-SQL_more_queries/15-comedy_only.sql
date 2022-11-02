-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT s.`title` FROM tv_shows AS s
INNER JOIN `tv_show_genres` AS g
ON g.`show_id` = s.`id`
INNER JOIN `tv_genres` AS t
ON t.`id` = g.`genre_id`
WHERE t.`name` = "Comedy"
ORDER BY s.`title`;
