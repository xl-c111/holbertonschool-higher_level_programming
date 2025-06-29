# Python - Object-relational mapping

A concise guide to using **MySQLdb** and **SQLAlchemy ORM** in Python for interacting with MySQL databases. Covers essential syntax, key concepts, and problem-solving strategies.

---

## 1 MySQLdb (Python MySQL Client)

### 1.1 Key Concepts

- `MySQLdb` is a lightweight Python interface to MySQL.
- Supports manual SQL query execution via cursors.

### 1.2 Common Cursor Methods

| Method              | Description                                           |
|---------------------|-------------------------------------------------------|
| `cursor.execute(sql)` | Executes a SQL query                               |
| `cursor.fetchone()`   | Fetches the next single row (as a tuple)           |
| `cursor.fetchall()`   | Fetches all remaining rows (as a list of tuples)   |
| `cursor.fetchmany(n)` | Fetches the next `n` rows (as a list of tuples)    |
| `cursor.close()`      | Closes the cursor                                   |

---
### 1.3 Safe SQL with Parameterized Queries in `MySQLdb`

#### 1.3.1 Basic Syntax

```python
cursor.execute(SQL_query, parameters)
```

- `parameters` must be:
  - a **tuple** or **list** when using `%s` placeholders.
  - a **dictionary** when using `%(name)s` placeholders.
---

#### 1.3.2 Using `%s` Placeholders (Positional Parameters)

Use a **tuple** or **list** to pass parameters.

##### ✅ Example

```python
query = "SELECT * FROM states WHERE name = %s AND id = %s"
params = ("Texas", 3)
cursor.execute(query, params)
```
---
#### 1.3.3 Using `%(name)s` Placeholders (Named Parameters)

Use a **dictionary** to pass named parameters.

##### ✅ Example

```python
query = "SELECT * FROM states WHERE name = %(state_name)s AND id = %(state_id)s"
params = {
    "state_name": "Texas",
    "state_id": 3
}
cursor.execute(query, params)
```
---
#### 1.3.4 Summary Table

| SQL Placeholder Type | Required Parameter Type | Example                             |
|----------------------|--------------------------|-------------------------------------|
| `%s`                 | Tuple or List            | `("Texas", 3)`                      |
| `%(name)s`           | Dictionary               | `{"state_name": "Texas"}`           |

----

### 1.4 Syntax Example

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

### 1.5 Problem-Solving Steps (MySQLdb)

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
- 2.3.1 Define ORM models with `__tablename__` and column attributes
- 2.3.2 Create an engine using `create_engine()`
  
   ##### 🧩 URL Components Explained
   | Part                  | Description |
   |-----------------------|-------------|
   | `dialect+driver`      | Database dialect and DBAPI driver (e.g., `mysql+mysqldb`) |
   | `username:password`   | Database user credentials |
   | `host:port`           | Hostname and port number of the database server |
   | `database`            | Name of the database to connect to |
   
   ##### 🧩 Example for MySQL:
   ```python
   from sqlalchemy import create_engine
   engine = create_engine("mysql+mysqldb://user:password@localhost:3306/my_database")
   ```

   ##### 🧩 Notes
  
   ###### `mysql+mysqldb`:

   - **`mysql`** is the *dialect* (i.e., the type of SQL being used).
   - **`mysqldb`** is the *DBAPI driver* that actually handles communication with the MySQL database.

   ###### `SQLAlchemy`:

   - Automatically manages **connection pooling**.
   - Reuses **engine connections** under the hood, improving efficiency and scalability.

- 2.3.3 Bind the session class via `sessionmaker()`
   ##### 🧩 Binding the Session
   To interact with the database, you need to bind the session to the engine and create session instances:

   ```python
   from sqlalchemy.orm import sessionmaker
   Session = sessionmaker(bind=engine)  # Create a session factory class
   session = Session()                  # Create a concrete session instance
   ```
   ##### 🧩 Explanation

   - `Session = sessionmaker(bind=engine)`  
   - Creates a **session factory class** that knows how to connect to the database using the given engine.

   - `session = Session()`  
   - Instantiates a **concrete session object** (i.e., opens a working connection to the database)

  ##### 🧩 Analogy

  Think of it like a factory pattern:

  | Concept                        | Analogy                     |
  |-------------------------------|-----------------------------|
  | `sessionmaker(bind=engine)`   | Setting up a session factory |
  | `Session`                     | The factory class            |
  | `Session()`                   | A new product (session instance) from the factory |
   
- 2.3.4 Use `.query() + .filter() + .order_by()` to construct queries
- 2.3.5 Use `.all()` or `.first()` to fetch results
- 2.3.6 Insert/update using `add()` / `update()` and call `commit()`
- 2.3.7 Always call `close()` to end the session

---
## 3 Pattern Matching with `like()` in SQL and SQLAlchemy

In SQL and SQLAlchemy, the `LIKE` operator is used for pattern matching in text columns. The most common wildcards are:

- `%` : Matches **any sequence of characters** (including none)
- `_` : Matches **a single character**

Below is a quick reference for how to use `like()` with patterns:

| Pattern Expression     | Meaning in SQL Terms                  | SQLAlchemy Usage Example                     |
|------------------------|---------------------------------------|----------------------------------------------|
| `%a%`                  | Contains the letter `a`               | `column.like('%a%')`                         |
| `a%`                   | Starts with `a`                       | `column.like('a%')`                          |
| `%a`                   | Ends with `a`                         | `column.like('%a')`                          |
| `_a%`                  | Second character is `a`               | `column.like('_a%')`                         |
| `%abc%`                | Contains substring `abc`              | `column.like('%abc%')`                       |
| `____`                 | Exactly four characters               | `column.like('____')`                        |
| `%` (only percent)     | Matches any value (not NULL)          | `column.like('%')`                           |

### Case Sensitivity

- `like()` is **case-sensitive**.
- Use `ilike()` in SQLAlchemy for **case-insensitive** matching (not supported by all databases).

**Example:**

```python
# Case-sensitive search (matches 'Alice' but not 'alice')
query.filter(User.name.like('A%'))

# Case-insensitive search (matches both 'Alice' and 'alice')
query.filter(User.name.ilike('a%'))
```
---

## 4 MySQLdb vs SQLAlchemy Comparison

| Feature                         | MySQLdb                          | SQLAlchemy ORM                     |
|----------------------------------|-----------------------------------|------------------------------------|
| Raw SQL support                  | ✅ Full control                    | ❌ Abstracted                      |
| Object-oriented access           | ❌ No                              | ✅ Yes                             |
| Suitable for quick scripts       | ✅ Lightweight                     | ⚠️ Verbose for simple use          |
| Transaction/session management   | Manual                            | Managed with session               |
| Query building                   | Manual SQL                        | Chainable Python methods           |

---

## 5 Full SQLAlchemy Query Example

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

## 6 Tips

- **Always call** `session.commit()` after using `add()`, `update()`, or `delete()` to persist changes in the database.
  ```python
  # Create a new State object
  new_state = State(name="Nevada")
  # Add it to the session (not yet saved in DB)
  session.add(new_state)
  # Persist the change in the database
  session.commit()  # ← without this, the new state won't be saved!
  ```
  
- **Use parameterized queries** when working with raw SQL in `MySQLdb` to avoid SQL injection. Even if there's only **one** parameter, you still need to pass it as a sequence (usually a tuple).

  ### ✅ Correct

  ```python
   cursor.execute("SELECT * FROM users WHERE username = %s", (user_input,))
   ```

   ### ❌ Incorrect

   ```python
   cursor.execute("SELECT * FROM users WHERE username = %s", (user_input))
   # This is just a string, not a tuple
   ```

   ### ✅ Explanation

   | Expression         | Type           |
   |--------------------|----------------|
   | `(user_input)`     | String         |
   | `(user_input,)`    | ✅ Tuple with 1 element |


- **Use** `.first()` **when expecting a single result** to reduce unnecessary memory and avoid list iteration:
  ```python
  user = session.query(User).filter(User.email == 'abc@example.com').first()
  ```

- **Keep sessions short-lived** and always close them after use to free up resources:
  ```python
  session.close()
  ```

- **Use** `pool_pre_ping=True` **in `create_engine()`** to avoid broken connections when the DB has timed out:
  ```python
  engine = create_engine(..., pool_pre_ping=True)
  ```

---
