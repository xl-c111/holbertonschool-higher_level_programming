-- Convert hbtn_0c_0 database to UTF8
USE hbtn_0c_0;

ALTER TABLE first_table
MODIFY name VARCHAR(256);

ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


"""
1, select the target database using USE
   - Syntax: USE database name

2, remove any column-level charset and collation, keep the column's type and length
   - Syntax: ATLER TABLE table_name
             MODIFY column_name column_type;

3, set the table's default charset and collation, apply it to relevant columns
   - Syntax: ATLER TABLE table_name
             CONVERT TO CHARACTER SET ... COLLATE ...

"""