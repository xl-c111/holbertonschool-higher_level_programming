# SQL - Introduction

This document provides a summary of commonly used SQL syntax in MySQL, based on practical examples such as data import, aggregation, filtering, and sorting.

## SQL Syntax Reference

This table summarizes key SQL syntax patterns used in MySQL, based on recent use cases.

| Syntax | Description | Example |
|--------|-------------|---------|
| `USE database_name;` | Select a database to work with | `USE hbtn_0c_0;` |
| `SHOW COLUMNS FROM table_name;` | View structure of a table | `SHOW COLUMNS FROM temperatures;` |
| `SELECT column1, column2 FROM table;` | Basic selection of columns | `SELECT city, value FROM temperatures;` |
| `AVG(column)` | Aggregate: calculate average | `AVG(value)` |
| `MAX(column)` | Aggregate: find maximum | `MAX(value)` |
| `GROUP BY column` | Group rows to apply aggregate functions | `GROUP BY city` |
| `ORDER BY column ASC\|DESC` | Sort results (ascending/descending) | `ORDER BY avg_temp DESC` |
| `LIMIT n` | Return only the first `n` rows | `LIMIT 3` |
| `BETWEEN A AND B` | Filter values in a closed range | `WHERE month BETWEEN 7 AND 8` |
| `WHERE condition` | Filter rows | `WHERE year = 2022 AND month = 7` |
| `ALTER TABLE table MODIFY column TYPE;` | Modify a column’s type or attributes | `MODIFY name VARCHAR(256);` |
| `ALTER TABLE table CONVERT TO CHARACTER SET charset COLLATE collation;` | Change table’s default charset and collation | `CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;` |
| `LOAD DATA INFILE 'file.csv' INTO TABLE table ...` | Import CSV data into table | See: [`LOAD DATA`](https://dev.mysql.com/doc/refman/8.0/en/load-data.html) |
| `SOURCE file.sql;` | Execute SQL from a file (MySQL shell only) | `SOURCE temperatures.sql;` |

---

## Notes

- `AVG()` and `MAX()` are aggregate functions, usually used with `GROUP BY`.
- `ORDER BY` works with any column, including aliases (e.g., `ORDER BY avg_temp DESC`).
- `LIMIT` must come **after** `ORDER BY` if both are used.
- To inherit a table’s default charset, use `MODIFY column_name TYPE` without specifying charset/collation.

