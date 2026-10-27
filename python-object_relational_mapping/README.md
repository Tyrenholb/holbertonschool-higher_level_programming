# Python - Object-relational mapping

Exercises using MySQLdb and SQLAlchemy to work with MySQL databases.

## Required execution environment

- Ubuntu 20.04 LTS with Python 3.8.5
- mysqlclient (MySQLdb) 2.0.x
- SQLAlchemy 1.4.x
- pycodestyle 2.7.x

The current development VM runs Ubuntu 26.04. Its project virtual
environment uses Python 3.8.20; it does not exactly match the required
execution environment. Its system `/usr/bin/python3` is Python 3.14.4.

## Local setup

```bash
python3.8 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

Use pip without sudo inside the virtual environment. Run scripts with
`python3 script.py` so they use that environment. Direct execution with
`./script.py` follows the required `/usr/bin/python3` shebang instead.

## Source checks

```bash
python3 -m pycodestyle --version
python3 -m pycodestyle *.py
wc -l *.py
```

Python source files must start with `#!/usr/bin/python3`, end with a
newline, and be executable. Modules, classes, and functions must have
sentence-length docstrings explaining their purpose. SQLAlchemy code
must not call `execute`.
