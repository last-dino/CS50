SELECT title FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
JOIN ratings ON movies.id = ratings.movie_id
WHERE (people.name = 'Jennifer Lawrence' OR people.name = 'Bradley Cooper')
GROUP BY title
HAVING COUNT(DISTINCT people.name) = 2;