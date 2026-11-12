# RESTful API - Fetching Posts

This project practises consuming a REST API from Python. It requests posts from
JSONPlaceholder, prints their titles, and exports selected fields to CSV.
The checked-in implementation is an API client, not a web server.

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
| [`task_02_requests.py`](task_02_requests.py) | Defines the two HTTP request helpers using `requests` and the standard-library `csv` module |
| [`main.py`](main.py) | Calls the print helper, then the CSV export helper |
| [`posts.csv`](posts.csv) | A tracked sample export with an `id,title,body` header and one post record |

`fetch_and_print_posts()` requests the posts endpoint and always prints
`Status Code: NUMBER` after receiving a response. For status `200`, it parses
the JSON list and prints each title on its own line.

`fetch_and_save_posts()` makes a separate request. For status `200`, it extracts
`id`, `title`, and `body` from every returned post, then writes them to
`posts.csv` in that column order. It does not print a completion message.
An empty list produces a header-only CSV file.

## Project dependency

This requests exercise uses the external `requests` package as a task-specific
dependency. `csv` is part of the standard library. There is no pinned dependency
file in this directory.

Use a Python 3.8 environment with a compatible `requests` installation. For a
new virtual environment, from the repository root:

```bash
cd restful-api
python3.8 -m venv .venv
source .venv/bin/activate
python -m pip install requests
```

Internet access is needed to reach the hard-coded endpoint:
`https://jsonplaceholder.typicode.com/posts`.

## Usage

From this directory with the environment active:

```bash
python3 -B main.py
```

The first line is `Status Code: 200` when the first request succeeds, followed
by one title per returned post. The second request writes `posts.csv`, replacing
its existing contents. Data and request outcomes depend on the external service;
the checked-in sample is not a promise of the next response's size or content.

To call the helpers individually:

```bash
python3 -B - <<'PYTHON'
from task_02_requests import fetch_and_print_posts

fetch_and_print_posts()
PYTHON
```

```bash
python3 -B - <<'PYTHON'
from task_02_requests import fetch_and_save_posts

fetch_and_save_posts()
PYTHON
```

The saved CSV has this header:

```csv
id,title,body
```

Fields containing commas or newlines are quoted by `csv.DictWriter`. A single
record can occupy multiple physical lines, as in the tracked sample.

## Checks and current status

With the required checker installed, run from this directory:

```bash
python3 --version
pycodestyle --version
pycodestyle main.py task_02_requests.py
```

Both tracked Python files end with a newline and parse on local Python 3.8.20.
They currently lack the required shebang and executable Git mode. The installed
pycodestyle 2.12.1 checker passes these files, but correction requires 2.7.x.

Local checks used mocked HTTP responses and temporary files to verify exact
status/title formatting, multi-post export, empty-list export, and non-200
behavior. Live requests were not made and the tracked `posts.csv` was preserved.

## Current limitations

- Requests have no explicit timeout and no exception handling for connection
  failures, invalid JSON, missing fields, or unexpected response shapes.
- For a non-200 response, the print helper prints only its status line. The
  save helper does nothing and leaves any existing CSV unchanged.
- The two helpers make independent requests, so their responses may differ.
- Both functions return `None`; they do not provide a success flag or the
  retrieved posts to the caller.
- `main.py` has no `if __name__ == "__main__"` guard. Importing it also makes
  both requests and can overwrite the CSV. Import the helper module instead
  when you only need the function definitions.
- The endpoint and export filename are fixed. `-B` prevents bytecode writes,
  but does not prevent CSV replacement.
