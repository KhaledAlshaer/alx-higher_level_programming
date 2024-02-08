-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.

SELECT s.title, GROUP_CONCAT(g.name) AS name
FROM tv_shows s
LEFT JOIN tv_show_genres m ON s.id = m.show_id
LEFT JOIN tv_genres g ON m.genre_id = g.id
GROUP BY s.title
ORDER BY s.title;

