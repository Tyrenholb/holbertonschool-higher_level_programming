# Python - Serialization

This project practises saving Python data to files and loading it again using
JSON, pickle, CSV, and XML. The exercises compare text-based formats with
Python object serialization and show how file handling affects types, return
values, and error handling.

## General requirements

- Corrections run on Ubuntu 20.04 LTS with Python 3.8.x.
- Every Python file must start exactly with `#!/usr/bin/env python3`.
- Python files must be executable and end with a newline.
- Code must follow PEP8, checked with pycodestyle 2.7.x.
- Output formatting must match the expected results exactly.
- External libraries are not allowed unless explicitly required by the task.

## Files and functions

| File | What it does |
| --- | --- |
| [`task_00_basic_serialization.py`](task_00_basic_serialization.py) | `serialize_and_save_to_file(data, filename)` writes JSON; `load_and_deserialize(filename)` reads it back |
| [`task_01_pickle.py`](task_01_pickle.py) | Defines `CustomObject` with name, age, and student status; supports display, pickle serialization, and class-method deserialization |
| [`task_02_csv.py`](task_02_csv.py) | `convert_csv_to_json(filename)` reads rows with `csv.DictReader` and writes a JSON list to `data.json` |
| [`task_03_xml.py`](task_03_xml.py) | `serialize_to_xml(dictionary, filename)` writes a `data` root and one child per entry; `deserialize_from_xml(filename)` reconstructs a dictionary |
| [`task_03_main.py`](task_03_main.py) | Runs the XML example with a name, age, and city, then prints the restored dictionary |

## Dependencies

Only standard-library modules are used: `json`, `pickle`, `csv`, and
`xml.etree.ElementTree`. No external runtime packages are needed. pycodestyle
is a separate checking tool required by the project standard.

## Usage

From the repository root, run the included XML demonstration:

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

The program creates or replaces `data.xml` in the working directory. `-B`
prevents Python from writing bytecode cache files during these examples.

### Save and restore JSON

From this directory:

```bash
python3 -B - <<'PYTHON'
from task_00_basic_serialization import (
    serialize_and_save_to_file, load_and_deserialize
)

serialize_and_save_to_file({"name": "Ada", "age": 28}, "sample.json")
print(load_and_deserialize("sample.json"))
PYTHON
```

Output:

```text
{'name': 'Ada', 'age': 28}
```

### Convert CSV to JSON

From the same directory:

```bash
printf 'name,age\nAda,28\n' > sample.csv
python3 -B - <<'PYTHON'
from task_02_csv import convert_csv_to_json

print(convert_csv_to_json("sample.csv"))
PYTHON
cat data.json
```

The example prints `True`, and `data.json` contains:

```json
[{"name": "Ada", "age": "28"}]
```

The JSON writer does not append a newline to this generated data file. The
source-file newline requirement is a separate check.

## Format behavior and limits

- JSON restores supported JSON types, so the integer age remains an integer
  in the JSON example. Unsupported objects and malformed input raise errors;
  these helpers do not catch them.
- Pickle preserves Python objects but can execute code while loading. Load
  only trusted pickle files whose required class definitions are available.
  `deserialize` catches selected file/unpickling errors and returns `None`;
  it does not catch every failure or verify the loaded object's class.
- `CustomObject.serialize` returns `None` both on success and for the errors
  it catches, so its return value is not a success flag.
- CSV values are strings. Conversion returns `True` on success or `False`
  for caught `OSError`/`EOFError` failures. Its output filename is always
  `data.json`, resolved from the current working directory.
- XML values are written with `str(value)` and read back as element text.
  Original numeric types are not restored. Keys must be suitable XML element
  names; the functions do not validate them or catch parse/file errors.
- Serialization writes replace existing output files. These examples do not
  implement a general nested-dictionary XML mapping.

## Checks and current status

With the required checker installed, run from this directory:

```bash
python3 --version
pycodestyle --version
pycodestyle *.py
```

All five Python files have the required shebang, end with a newline, and parse
on local Python 3.8.20. None currently has the executable Git mode. The installed
pycodestyle 2.12.1 checker reports a long line in `task_02_csv.py` and missing
blank lines in `task_03_main.py`; correction requires pycodestyle 2.7.x.

JSON, pickle, CSV, and XML round trips, selected failure returns, and the exact
XML demonstration output were checked locally using temporary files.

## Clean up

Remove only the sample files created by the examples when finished:

```bash
rm -f data.xml sample.json sample.csv data.json
```
