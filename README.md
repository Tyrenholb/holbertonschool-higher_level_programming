# Python - Higher Level Programming

This repository contains my Holberton School projects on Python serialization,
object relational mapping, and consuming a REST API. The exercises practise
working with files, mapping database records to objects, handling structured
data, and formatting output exactly as required.

Each project folder has a README describing its files, setup, usage, and
current limitations.

## Project folders

| Folder | What it covers |
| --- | --- |
| [`python-object_relational_mapping`](python-object_relational_mapping/README.md) | Direct MySQL queries with MySQLdb, parameterized inputs, SQLAlchemy models, state/city joins, and database creation/read/update/delete exercises |
| [`python-serialization`](python-serialization/README.md) | Saving and restoring data with JSON, pickle, CSV, and XML; type differences, file handling, and selected error cases |
| [`restful-api`](restful-api/README.md) | Fetching JSONPlaceholder posts with `requests`, printing titles, and exporting post fields to CSV |

## General requirements

- Corrections run on Ubuntu 20.04 LTS.
- The correction interpreter is Python 3.8.x.
- Every Python file must start exactly with:

```python
#!/usr/bin/env python3
```

- Every Python file must be executable and end with a newline.
- Code must follow PEP8, checked with pycodestyle 2.7.x.
- Output must match the expected formatting exactly.
- External libraries are not allowed unless explicitly requested by the task.

These requirements describe the submission standard. They do not mean that
all checked-in files currently meet it; known differences are documented below
and in the project READMEs.

## Dependencies

| Project | Runtime dependencies |
| --- | --- |
| Serialization | Python standard library only: `json`, `pickle`, `csv`, and `xml.etree.ElementTree` |
| Object relational mapping | MySQL server, `mysqlclient` for MySQLdb, and SQLAlchemy; versions are pinned in the project's `requirements.txt` |
| REST requests | The task-specific `requests` package and internet access; CSV handling uses the standard library |

Use external packages only for the tasks that require them. pycodestyle is a
checking tool, separate from the programs' runtime dependencies. Project
READMEs describe environment setup and database prerequisites.

## Running a project

There is no single entry point for the repository. Some files expose functions
for a caller; others run demonstrations, query a database, or make HTTP requests.

For a standard-library-only example, run the XML demonstration from the
repository root:

```bash
cd python-serialization
python3 -B task_03_main.py
```

Output:

```text
Dictionary serialized to data.xml

Deserialized Data:
{'name': 'John', 'age': '28', 'city': 'New York'}
```

This creates or replaces `data.xml` in the current working directory. `-B`
prevents bytecode cache writes, not data-file changes.

Use each folder's instructions for other tasks. ORM scripts need an existing
MySQL database and positional credentials. The REST driver makes two requests
and can replace its CSV output.

## Checking the requirements

Confirm the interpreter and checker versions in your selected environment:

```bash
python3 --version
pycodestyle --version
```

They should report Python 3.8.x and pycodestyle 2.7.x for correction. Run the
style checker on the project being submitted, for example:

```bash
pycodestyle python-serialization/*.py
```

Check shebangs, executable permissions, and final newlines separately from
style. For a source file whose executable mode needs to be set, the command is
`chmod +x FILE.py`. Invoking a file through `python3` does not prove that it can
be executed directly or that its interpreter line is correct.

## Current verification and limitations

- All 24 tracked Python files parse on local Python 3.8.20 and end with a
  newline. This is not a complete Ubuntu 20.04 correction run.
- ORM files use `#!/usr/bin/python3` rather than the required environment-based
  shebang. The two REST Python files lack a shebang. Serialization files use
  the required line.
- `6-model_state.py`, all five serialization Python files, and both REST Python
  files lack the executable Git mode.
- The installed style checker is pycodestyle 2.12.1, rather than 2.7.x. It
  reports a long line in the CSV serialization task and missing blank lines
  in the XML driver. The tracked ORM and REST sources pass that local checker.
- Serialization examples were verified with temporary files, including exact
  XML demonstration output. REST behavior was checked with mocked responses;
  live requests and database operations were not run.
- Data-writing functions can replace files, ORM mutation scripts change
  database records, and pickle loading must be limited to trusted files.

Earlier bytecode cache files and a sample REST CSV are tracked artifacts, not
proof of compliance or a substitute for checking the Python source. See the
individual READMEs for detailed behavior and task-specific limitations.
