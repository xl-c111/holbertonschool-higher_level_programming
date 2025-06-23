-- List the number of records with the same score in the table second_table
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY COUNT(*) DESC;



"""
1, SELECT score, COUNT(*) AS number - tell the database to return two columns: 
   - score: the actual score value in the table
   - COUNT(*) the number of time each unique appears, it's renamed using 'AS number'

2, GROUP BY score
   - group rows by their score value, all rows with the same value treated as a group.
     The COUNT(*) function is then applied to each group

3, ORDER BY COUNT(*) DESC
   - orders the result in desc order by the number of rows in each group
"""
