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

