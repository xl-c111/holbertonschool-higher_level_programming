# 📘 SQL - Introduction

This document provides a summary of commonly used SQL syntax in MySQL, based on practical examples such as database creation, table operations, aggregation, filtering, sorting, and more.

---

## 🛠️ Basic SQL Operations

| Syntax | Description | Example |
|--------|-------------|---------|
| `CREATE DATABASE db_name;` | Create a new database | `CREATE DATABASE hbtn_0c_0;` |
| `DROP DATABASE db_name;` | Delete a database | `DROP DATABASE hbtn_0c_0;` |
| `USE db_name;` | Select a database to work with | `USE hbtn_0c_0;` |
| `SHOW TABLES;` | List all tables in the current database | `SHOW TABLES;` |
| `CREATE TABLE table (...);` | Create a new table with specified columns | `CREATE TABLE first_table (id INT, name VARCHAR(256));` |
| `DESCRIBE table;` or `SHOW COLUMNS FROM table;` | Show the structure of a table | `DESCRIBE first_table;` |
| `SELECT * FROM table;` | List all rows in a table | `SELECT * FROM first_table;` |
| `INSERT INTO table (col1, col2) VALUES (...);` | Insert a new row into the table | `INSERT INTO first_table (id, name) VALUES (89, 'Best');` |
| `SELECT COUNT(*) FROM table WHERE condition;` | Count how many records match a condition | `SELECT COUNT(*) FROM first_table WHERE id = 89;` |
| `SELECT column1, column2 FROM table;` | Select specific columns from the table | `SELECT city, value FROM temperatures;` |
| `UPDATE table SET col = val WHERE condition;` | Update rows in the table | `UPDATE first_table SET score = 10 WHERE name = 'Bob';` |
| `DELETE FROM table WHERE condition;` | Delete rows that match the condition | `DELETE FROM first_table WHERE score <= 5;` |

---

## 📊 SQL Aggregation & Filtering

| Syntax | Description | Example |
|--------|-------------|---------|
| `AVG(column)` | Aggregate: calculate average | `AVG(value)` |
| `MAX(column)` | Aggregate: find maximum | `MAX(value)` |
| `GROUP BY column` | Group rows to apply aggregate functions | `GROUP BY city` |
| `ORDER BY column ASC\|DESC` | Sort results (ascending/descending) | `ORDER BY avg_temp DESC` |
| `LIMIT n` | Return only the first `n` rows | `LIMIT 3` |
| `BETWEEN A AND B` | Filter values in a closed range | `WHERE month BETWEEN 7 AND 8` |
| `WHERE condition` | Filter rows | `WHERE year = 2022 AND month = 7` |

---

## 🔧 Charset & File Import

| Syntax | Description | Example |
|--------|-------------|---------|
| `ALTER TABLE table MODIFY column TYPE;` | Modify a column’s type or attributes | `MODIFY name VARCHAR(256);` |
| `ALTER TABLE table CONVERT TO CHARACTER SET charset COLLATE collation;` | Change table’s default charset and collation | `CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;` |
| `LOAD DATA INFILE 'file.csv' INTO TABLE table ...` | Import CSV data into table | See: [`LOAD DATA`](https://dev.mysql.com/doc/refman/8.0/en/load-data.html) |
| `SOURCE file.sql;` | Execute SQL from a file (MySQL shell only) | `SOURCE temperatures.sql;` |

---

## 📌 Notes

- `GROUP BY` is almost always used with aggregate functions (`AVG()`, `MAX()`, `COUNT()`, etc.).
- `ORDER BY` controls result ordering; `ASC` (ascending) is the default, use `DESC` for descending.
- `LIMIT` must come **after** `ORDER BY` when both are used.
- `MODIFY column TYPE` (without charset) removes explicit charset and makes the column inherit the table default.
