-- List all records of the table second_table
SELECT score, name FROM second_table
WHERE name IS NOT NULL and name != ""
ORDER BY score DESC;