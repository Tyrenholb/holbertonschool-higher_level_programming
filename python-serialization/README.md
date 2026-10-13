# Python Serialization

Practice saving and restoring Python data using JSON, pickle, CSV, and XML.

## Tasks

| File | Description |
| --- | --- |
| `task_00_basic_serialization.py` | Save a dictionary to JSON and load it back. |
| `task_01_pickle.py` | Serialize and restore custom class instances using pickle. Handle missing or malformed files. |
| `task_02_csv.py` | Read CSV rows as dictionaries and write them to `data.json`. Return whether conversion succeeded. |
| `task_03_xml.py` | Convert dictionary entries into XML elements and reconstruct a dictionary from an XML file. |

## Concepts Practised

- Serialization and deserialization.
- Text and binary file handling.
- Exception handling and return values.
- Using `json`, `pickle`, `csv`, and `xml.etree.ElementTree`.
- Understanding type differences: CSV values and XML element text are read as strings, while pickle preserves Python object types.

Only load pickle files from trusted sources, as unpickling can execute code.
