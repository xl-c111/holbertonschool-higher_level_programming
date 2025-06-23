-- Display the max temperature of each state (ordered by State name)
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY state
ORDER BY state ASC;





"""
1, import a table dump: 
cat temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0

2, MAX(value): a function returns the highest value

3, ORDER BY state ASC: sort the result by state column in ascending(A to Z) order 
"""