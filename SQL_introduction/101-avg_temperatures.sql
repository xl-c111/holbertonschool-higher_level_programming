-- Display the average temperature by city ordered by temperature (descending)
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;


"""
1, check the structure of the table(run the command line below in the terminal)
echo "SHOW COLUMNS FROM temperatures;" | mysql -hlocalhost -uroot -p hbtn_0c_0 == USE 

2, SELECT city, AVG(value) as avg_temp
   - SELECT: tell MYSQL which column to return 
   - AVG(value): a function that calculates average of the value column
   - as avg_temp: assign a label for the result of AVG(value) to display

3, FROM table_name: specify the table where the data comes from

4, GROUP by column_name: put rows with the same column_name together; AVG(value) finds the average temp for each city

5, ORDER BY column_name: sort the whole result by column_name, from highest to lowest
"""