-- Display the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month BETWEEN 7 AND 8
GROUP BY city
ORDER BY avg_temp DESC
Limit 3;


"""
1, WHERE month BETWEEN...AND...: only include the month column 7 and 8
== WHERE month >= 7 AND month <= 8

2, Limit 3: only return the first 3 rows
"""