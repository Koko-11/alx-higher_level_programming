-- Lists all shows in hbtn_0d_tvshows that have at least one genre linked.
-- Records are sorted by ascending tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
