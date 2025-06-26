-- List all cities of California that can be found in the database hbtn_0d_usa
SELECT id, name
FROM cities
-- filter only row from cities where state_id matches the subquery 
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY cities.id ASC;



