# Python - Object Relational Mapping

This project connects Python to MySQL, first with direct SQL through MySQLdb,
then by mapping rows to Python objects with SQLAlchemy. The exercises query
states and cities, filter user-supplied names, and practise inserting, updating,
and deleting records.

## General requirements

- Corrections run on Ubuntu 20.04 LTS with Python 3.8.x.
- Every Python file must start exactly with `#!/usr/bin/env python3`.
- Python files must be executable and end with a newline.
- Code must follow PEP8, checked with pycodestyle 2.7.x.
- Output formatting must match the expected results exactly.
- External libraries are not allowed unless explicitly required by the task.

## Scripts and models

| File | What it does |
| --- | --- |
| [`0-select_states.py`](0-select_states.py) | Prints all state rows as tuples, ordered by ID |
| [`1-filter_states.py`](1-filter_states.py) | Prints states beginning with uppercase `N`, using a binary name comparison |
| [`2-my_filter_states.py`](2-my_filter_states.py) | Matches a name using direct string interpolation into SQL; demonstrates the unsafe approach |
| [`3-my_safe_filter_states.py`](3-my_safe_filter_states.py) | Matches a name using bound parameters instead of SQL interpolation |
| [`4-cities_by_state.py`](4-cities_by_state.py) | Prints city ID, city name, and state name tuples, ordered by city ID |
| [`5-filter_cities.py`](5-filter_cities.py) | Prints a state's city names separated by comma-space, ordered by city ID |
| [`model_state.py`](model_state.py) | Defines the shared declarative `Base` and the `State` model for `states` |
| [`6-model_state.py`](6-model_state.py) | Creates missing tables in the imported model metadata; currently imports the State model only |
| [`7-model_state_fetch_all.py`](7-model_state_fetch_all.py) | Prints all states as `id: name`, ordered by ID |
| [`8-model_state_fetch_first.py`](8-model_state_fetch_first.py) | Prints the lowest-ID state, or `Nothing` if none exists |
| [`9-model_state_filter_a.py`](9-model_state_filter_a.py) | Prints states matching `%a%`, ordered by ID |
| [`10-model_state_my_get.py`](10-model_state_my_get.py) | Prints the first matching state's ID, or `Not found` |
| [`11-model_state_insert.py`](11-model_state_insert.py) | Adds a Louisiana row, commits it, and prints its ID |
| [`12-model_state_update_id_2.py`](12-model_state_update_id_2.py) | Renames state ID `2` to New Mexico if it exists, then commits |
| [`13-model_state_delete_a.py`](13-model_state_delete_a.py) | Deletes states matching `%a%` and commits |
| [`model_city.py`](model_city.py) | Defines `City`, including its foreign key to `states.id` |
| [`14-model_city_fetch_by_state.py`](14-model_city_fetch_by_state.py) | Joins states and cities; prints `state: (city_id) city`, ordered by city ID |
| [`14-model_city_fetch_by_state.sql`](14-model_city_fetch_by_state.sql) | Creates and populates the task-14 sample database |
| [`requirements.txt`](requirements.txt) | Pins mysqlclient 2.0.3, SQLAlchemy 1.4.22, and pycodestyle 2.7.0 |

The model names are limited to 128 characters in Python. The supplied SQL seed
uses 256-character name columns, so its schema is not identical to the models.

## Project dependencies

These ORM exercises use MySQLdb, supplied by `mysqlclient`, and SQLAlchemy as
task-specific external dependencies. They also need a MySQL server listening
on `localhost:3306` and an account with access to the selected database.

From the repository root, create an isolated environment and install the
pinned dependencies:

```bash
cd python-object_relational_mapping
python3.8 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Building mysqlclient may require MySQL client development headers and compiler
tools on the host. The environment does not create a MySQL database or account.

## Usage

Scripts accept a MySQL username, password, and database name, in that order.
Name-search scripts also require a fourth argument. Replace the uppercase
placeholders below with your exercise credentials and an existing database:

```bash
python3 0-select_states.py USER PASSWORD DATABASE
python3 3-my_safe_filter_states.py USER PASSWORD DATABASE "New York"
python3 5-filter_cities.py USER PASSWORD DATABASE "California"
python3 7-model_state_fetch_all.py USER PASSWORD DATABASE
python3 10-model_state_my_get.py USER PASSWORD DATABASE "New York"
```

Results depend on the database contents. A matching state with ID `4` would
print as `(4, 'New York')` in the direct state-query scripts, as `4: New York`
in the state-list ORM scripts, and as `4` in task 10. Task 5 prints only a
comma-separated city list and prints an empty line when no cities match.

### Task 14 sample database

The included setup SQL targets `hbtn_0e_14_usa`. Use it on a disposable exercise
database through an account with the required creation and insertion privileges:

```bash
mysql -u USER -p < 14-model_city_fetch_by_state.sql
python3 14-model_city_fetch_by_state.py USER PASSWORD hbtn_0e_14_usa
```

On a fresh database initialized by that file, the first output line is:

```text
California: (1) San Francisco
```

The SQL uses conditional database/table creation, but its inserts run every
time. Repeating it adds rows and can make the intended ID assumptions incorrect.
The earlier tasks also need their expected tables and data; their individual
setup SQL files are not included here.

## Checks

With the project environment active, run from this directory:

```bash
python3 --version
pycodestyle --version
pycodestyle *.py
```

Confirm Python 3.8.x and pycodestyle 2.7.x for the correction toolchain.
The required interpreter line is:

```python
#!/usr/bin/env python3
```

Local inspection found that all 17 tracked Python files instead use
`#!/usr/bin/python3`; `6-model_state.py` also lacks the executable Git mode.
All files end with a newline and parse on local Python 3.8.20. They pass the
installed pycodestyle 2.12.1 checker, but that is not the required checker
version. Live MySQL/ORM operations were not verified in this documentation pass.

## Data changes and limits

- Task 2 interpolates input into SQL. Use task 3's parameterized approach for
  user-supplied names rather than treating task 2 as a safe query template.
- Task 6 creates tables in an existing database; it does not create the database
  itself or register City unless that model is imported.
- Tasks 11, 12, and 13 modify stored data. Repeating task 11 adds another row;
  deletions may be affected by foreign-key constraints when cities refer to states.
- SQLAlchemy `LIKE` and equality comparisons follow the database collation;
  do not assume the same case sensitivity as the direct binary comparisons.
- The scripts assume correctly ordered command-line arguments and do not add
  custom handling for connection failures or invalid credentials.
- Task 2 references `db.close` without calling it; task 9 likewise references
  `session.close` without calling it. These are current cleanup limitations.
