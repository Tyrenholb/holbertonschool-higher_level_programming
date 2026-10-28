# Python – Object Relational Mapping

This Holberton project connects Python to MySQL using **MySQLdb** for direct SQL queries and **SQLAlchemy** for working with database rows as Python objects.

## Topics covered

- Selecting, filtering, and sorting records.
- Parameterized queries and SQL injection prevention.
- Mapping tables to classes with SQLAlchemy.
- Creating, reading, updating, and deleting records.
- Foreign keys and joins between states and cities.

## Files

| Files | Purpose |
| --- | --- |
| `0-select_states.py` – `5-filter_cities.py` | Direct SQL queries, name filters, safe parameters, and city/state joins. |
| `model_state.py` | Defines the shared `Base` and the `State` model. |
| `6-model_state.py` | Creates tables defined by the imported models. |
| `7-model_state_fetch_all.py` – `10-model_state_my_get.py` | Retrieves all states, the first state, or states matching a condition. |
| `11-model_state_insert.py` | Adds Louisiana and prints its generated ID. |
| `12-model_state_update_id_2.py` | Renames state ID 2 to New Mexico. |
| `13-model_state_delete_a.py` | Deletes states whose names contain `a`. |
| `model_city.py` | Defines `City`, with a foreign key to `states.id`. |
| `14-model_city_fetch_by_state.py` | Lists cities with their state names, ordered by city ID. |
| `14-model_city_fetch_by_state.sql` | Creates and populates the database for task 14. |
| `requirements.txt` | Lists the project dependencies. |

Task 2 demonstrates unsafe string interpolation; task 3 uses bound parameters to prevent SQL injection.

## Requirements

- Python 3.8 and a MySQL server on `localhost:3306`.
- mysqlclient 2.0.3, SQLAlchemy 1.4.22, and pycodestyle 2.7.0.

Install dependencies in your virtual environment:

```bash
python -m pip install -r requirements.txt
```

## Usage

Create and populate the relevant database before running a script. Scripts accept a MySQL username, password, and database name; search scripts also accept a name.

```bash
python 7-model_state_fetch_all.py USER PASSWORD hbtn_0e_6_usa
python 10-model_state_my_get.py USER PASSWORD hbtn_0e_6_usa "New York"
```

For task 14:

```bash
mysql -u USER -p < 14-model_city_fetch_by_state.sql
python 14-model_city_fetch_by_state.py USER PASSWORD hbtn_0e_14_usa
```

Insertion, update, and deletion scripts modify stored data. Running the insertion script again adds another Louisiana row.

