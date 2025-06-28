# Python - Object-relational mapping

A concise guide to using **MySQLdb** and **SQLAlchemy ORM** in Python for interacting with MySQL databases. Covers essential syntax, key concepts, and problem-solving strategies.

---

## 1 MySQLdb (Python MySQL Client)

### 1.1 Key Concepts

- `MySQLdb` is a lightweight Python interface to MySQL.
- Supports manual SQL query execution via cursors.

### 1.2 Syntax Example

```python
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="my_db")
cursor = db.cursor()

cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
db.close()
```
---

### 1.3 Problem-Solving Steps (MySQLdb)

1. Connect to MySQL using `MySQLdb.connect()`
2. Create a cursor with `cursor()`
3. Write and execute raw SQL with `execute()`
4. Fetch results using `fetchall()`
5. Always close cursor and database with `cursor.close()` and `db.close()`

---

## 2 SQLAlchemy ORM

### 2.1 Key Concepts

- **Object Relational Mapping (ORM):** Maps Python classes to SQL tables
- Enables clean, maintainable, and object-oriented interactions with relational databases

---

### 2.2 Common SQLAlchemy Syntax

| SQLAlchemy Syntax                                   | Equivalent SQL                      | Description               |
|-----------------------------------------------------|-------------------------------------|---------------------------|
| `session.query(Model)`                              | `SELECT * FROM table`               | Query all records         |
| `.filter(Model.name == 'California')`               | `WHERE name = 'California'`         | Filter results            |
| `.order_by(Model.id.asc())`                         | `ORDER BY id ASC`                   | Sort ascending            |
| `.first()`                                          | `LIMIT 1`                           | Get first record          |
| `.all()`                                            | *(returns all as list)*             | Get all records           |
| `.add(obj)`                                         | `INSERT INTO ...`                   | Insert one record         |
| `.add_all([obj1, obj2])`                            | `INSERT INTO ...` (multiple rows)   | Insert multiple records   |
| `.update({field: value})`                           | `UPDATE ... SET ...`                | Update record(s)          |
| `.delete(obj)`                                      | `DELETE FROM ...`                   | Delete a record           |
| `.commit()`                                         | `COMMIT;`                           | Save changes              |
| `.close()`                                          | *(no SQL equivalent)*               | Close the session         |

---

### 2.3 Problem-Solving Strategy (SQLAlchemy)

1. Define ORM models with `__tablename__` and column attributes
2. Create an engine using `create_engine()`
3. Bind the session class via `sessionmaker()`
4. Use `.query() + .filter() + .order_by()` to construct queries
5. Use `.all()` or `.first()` to fetch results
6. Insert/update using `add()` / `update()` and call `commit()`
7. Always call `close()` to end the session

---

## 3 MySQLdb vs SQLAlchemy Comparison

| Feature                         | MySQLdb                          | SQLAlchemy ORM                     |
|----------------------------------|-----------------------------------|------------------------------------|
| Raw SQL support                  | ✅ Full control                    | ❌ Abstracted                      |
| Object-oriented access           | ❌ No                              | ✅ Yes                             |
| Suitable for quick scripts       | ✅ Lightweight                     | ⚠️ Verbose for simple use          |
| Transaction/session management   | Manual                            | Managed with session               |
| Query building                   | Manual SQL                        | Chainable Python methods           |

---

## 4 Full SQLAlchemy Query Example

```python
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

def fetch_states(username, password, database):
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id.asc()).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
```

---

## 5 Tips

- 5.1 **Always call** `session.commit()` after using `add()`, `update()`, or `delete()` to persist changes in the database.
  ```python
  # Create a new State object
  new_state = State(name="Nevada")
  # Add it to the session (not yet saved in DB)
  session.add(new_state)
  # Persist the change in the database
  session.commit()  # ← without this, the new state won't be saved!
  ```
  
- 5.2 **Use parameterized queries** when working with raw SQL in `MySQLdb` to avoid SQL injection:
  ```python
  cursor.execute("SELECT * FROM states WHERE name = %s", ('Texas',))
  ```

- 5.3 **Use** `.first()` **when expecting a single result** to reduce unnecessary memory and avoid list iteration:
  ```python
  user = session.query(User).filter(User.email == 'abc@example.com').first()
  ```

- 5.4 **Keep sessions short-lived** and always close them after use to free up resources:
  ```python
  session.close()
  ```

- 5.5 **Use** `pool_pre_ping=True` **in `create_engine()`** to avoid broken connections when the DB has timed out:
  ```python
  engine = create_engine(..., pool_pre_ping=True)
  ```

---
