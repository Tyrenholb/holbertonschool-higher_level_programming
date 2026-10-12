#!/usr/bin/env python3
"""Converting CSV Data to JSON Format"""


import json
import csv


def convert_csv_to_json(filename):
    data = []
    try:
        with open(filename, "r", encoding="utf-8", newline="") as f_csv:
            csv_reader = csv.DictReader(f_csv)
            for row in csv_reader:
                data.append(row)

        with open("data.json", "w", encoding='utf-8') as f_json:
            json.dump(data, f_json)
            return True
    except (OSError, EOFError):
        return False
