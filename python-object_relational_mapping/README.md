# Python - Object-relational mapping
## 🧰 SQLAlchemy vs SQL Syntax Cheat Sheet

This table provides a quick reference comparing common SQLAlchemy ORM methods to their SQL equivalents.

| SQLAlchemy ORM Syntax                                | Equivalent SQL Syntax                             | Description                                                  |
|------------------------------------------------------|---------------------------------------------------|--------------------------------------------------------------|
| `session.query(Model)`                               | `SELECT * FROM table_name;`                       | Query all rows from a table                                  |
| `session.query(Model).filter(Model.id == 5)`         | `SELECT * FROM table_name WHERE id = 5;`          | Filter rows by condition                                     |
| `session.query(Model).filter(Model.id > 10)`         | `SELECT * FROM table_name WHERE id > 10;`         | Filter with comparison operators                             |
| `session.query(Model).filter(Model.name.like('A%'))` | `SELECT * FROM table_name WHERE name LIKE 'A%';`  | Pattern matching with LIKE                                   |
| `session.query(Model).filter(Model.id.in_([1,2,3]))` | `SELECT * FROM table_name WHERE id IN (1,2,3);`   | Filter rows with a list of values                           |
| `session.query(Model).order_by(Model.id.asc())`      | `ORDER BY id ASC`                                 | Sort ascending                                               |
| `session.query(Model).order_by(Model.name.desc())`   | `ORDER BY name DESC`                              | Sort descending                                              |
| `session.query(Model).first()`                       | `SELECT * FROM table_name LIMIT 1;`               | Get the first result only                                    |
| `session.query(Model).all()`                         | *(no direct SQL equivalent)*                      | Fetch all results as a list of objects                      |
| `session.query(Model).count()`                       | `SELECT COUNT(*) FROM table_name;`                | Count rows                                                   |
| `session.query(Model).distinct()`                    | `SELECT DISTINCT column FROM table_name;`         | Select distinct values                                       |
| `session.add(obj)`                                   | `INSERT INTO table_name (...) VALUES (...);`      | Add one record                                               |
| `session.add_all([obj1, obj2])`                      | Multiple `INSERT` statements                      | Add multiple records at once                                 |
| `session.query(Model).update({field: value})`        | `UPDATE table_name SET field = value;`            | Update rows                                                  |
| `session.delete(obj)`                                | `DELETE FROM table_name WHERE ...;`               | Delete a specific row                                        |
| `session.commit()`                                   | *(no direct SQL equivalent)*                      | Commit all pending operations                                |
| `session.close()`                                    | *(no direct SQL equivalent)*                      | Close session, release DB connection                         |

---

### 🔍 Notes

- SQLAlchemy uses Python objects to represent tables and rows.
- Methods like `.filter()`, `.all()`, `.first()` etc. chain together to form a query.
- Always call `session.commit()` to save `add()`, `update()`, or `delete()` changes.
- Use `session.close()` to free resources when done.

---

### 📚 Example

```python
# Query all states ordered by ID
states = session.query(State).order_by(State.id.asc()).all()
for state in states:
    print(f"{state.id}: {state.name}")
```
Equivalent SQL:
```
SELECT * FROM states ORDER BY id ASC;
```
