# 🔐 SQL - More queries

> This document summarizes key syntax and usage examples for managing MySQL user permissions, based on tutorials from DigitalOcean and MySQLTutorial.org.

---

## 📘 GRANT Syntax

```sql
GRANT privilege [, privilege] ON privilege_level TO 'username'@'host' [WITH GRANT OPTION];
```

- **privilege**: The type of access (e.g., SELECT, INSERT, UPDATE).
- **privilege_level**: Scope of the privilege:
  - `*.*`: Global level (all databases and tables)
  - `database_name.*`: Database level
  - `database_name.table_name`: Table level
- **'username'@'host'**: MySQL user and host specification.
- **WITH GRANT OPTION**: Allows the user to grant privileges to others.

---

## 🔑 Common Privileges

| Privilege          | Description                                 |
|--------------------|---------------------------------------------|
| `ALL PRIVILEGES`   | Grants all privileges except GRANT OPTION  |
| `SELECT`           | Read table data                            |
| `INSERT`           | Insert data into table                     |
| `UPDATE`           | Update existing table data                 |
| `DELETE`           | Delete rows from table                     |
| `CREATE`           | Create databases or tables                 |
| `DROP`             | Delete databases or tables                 |
| `ALTER`            | Modify table structure                     |
| `INDEX`            | Create or drop indexes                     |
| `GRANT OPTION`     | Allow user to grant privileges to others   |
| `EXECUTE`          | Execute stored procedures and functions    |
| `PROXY`            | Allow user to impersonate another account  |

---

## 🧪 Examples

### 1. Create a User

```sql
CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';
```

### 2. Grant Permissions

```sql
-- Grant all privileges on all databases (with ability to grant others)
GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'localhost' WITH GRANT OPTION;

-- Grant all privileges on a specific database
GRANT ALL PRIVILEGES ON my_database.* TO 'newuser'@'localhost';

-- Grant SELECT and INSERT on one table
GRANT SELECT, INSERT ON my_database.my_table TO 'newuser'@'localhost';

-- Grant column-specific privileges
GRANT SELECT (col1, col2) ON my_database.my_table TO 'newuser'@'localhost';

-- Grant EXECUTE on a stored procedure
GRANT EXECUTE ON PROCEDURE my_database.my_procedure TO 'newuser'@'localhost';

-- Grant proxy privilege
GRANT PROXY ON 'otheruser'@'localhost' TO 'newuser'@'localhost';
```

### 3. Revoke Permissions

```sql
-- Revoke SELECT from a table
REVOKE SELECT ON my_database.my_table FROM 'newuser'@'localhost';

-- Revoke all privileges and grant option
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'newuser'@'localhost';
```

### 4. Check Privileges

```sql
SHOW GRANTS FOR 'newuser'@'localhost';
```

### 5. Apply Changes

```sql
FLUSH PRIVILEGES;
```

---

## 🔗 SQL JOINs with Set Theory Notation

> This document maps SQL JOIN operations to set theory concepts like intersections (∩), unions (∪), and differences (−), with SQL syntax and interpretation.

---

### 1. `INNER JOIN` → A ∩ B

**Set Meaning:**  
Only elements common to both tables A and B.

**SQL:**
```sql
SELECT *
FROM A
INNER JOIN B
ON A.key = B.key;
```

**Result:**  
Returns rows where keys exist in both A and B.

---

### 2. `LEFT JOIN` → A ∪ (A − B)

**Set Meaning:**  
All elements from A, and matching elements from B. Unmatched B values are NULL.

**SQL:**
```sql
SELECT *
FROM A
LEFT JOIN B
ON A.key = B.key;
```

**Result:**  
All rows from A, with matched B data if exists, otherwise NULL.

---

### 3. `LEFT JOIN` with `WHERE B.key IS NULL` → A − B

**Set Meaning:**  
Only elements in A that do not exist in B.

**SQL:**
```sql
SELECT *
FROM A
LEFT JOIN B
ON A.key = B.key
WHERE B.key IS NULL;
```

**Result:**  
Only rows in A that have no match in B.

---

### 4. `RIGHT JOIN` → B ∪ (B − A)

**Set Meaning:**  
All elements from B, and matching elements from A. Unmatched A values are NULL.

**SQL:**
```sql
SELECT *
FROM A
RIGHT JOIN B
ON A.key = B.key;
```

**Result:**  
All rows from B, with matched A data if exists, otherwise NULL.

---

### 5. `RIGHT JOIN` with `WHERE A.key IS NULL` → B − A

**Set Meaning:**  
Only elements in B that do not exist in A.

**SQL:**
```sql
SELECT *
FROM A
RIGHT JOIN B
ON A.key = B.key
WHERE A.key IS NULL;
```

**Result:**  
Only rows in B that have no match in A.

---

### 6. `FULL OUTER JOIN` → A ∪ B

**Set Meaning:**  
All elements from both A and B.

**SQL:**
```sql
SELECT *
FROM A
FULL OUTER JOIN B
ON A.key = B.key;
```

**Result:**  
All rows from A and B, matched where possible, otherwise NULLs.

---

### 7. `FULL OUTER JOIN` with `WHERE A.key IS NULL OR B.key IS NULL` → (A − B) ∪ (B − A)

**Set Meaning:**  
Elements in A or B that have no match in the other.

**SQL:**
```sql
SELECT *
FROM A
FULL OUTER JOIN B
ON A.key = B.key
WHERE A.key IS NULL OR B.key IS NULL;
```

**Result:**  
Rows only from A or B with no matching pair.

---
