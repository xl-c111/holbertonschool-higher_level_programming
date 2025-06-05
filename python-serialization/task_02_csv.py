#!/usr/bin/python3
"""This module provides a function to convert CSV files to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename, json_filename="data.json"):
    """ Convert a CSV file to JSON format."""
    try:
        with open(csv_filename, "r", newline="") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        with open(json_filename, "w") as f:
            json.dump(rows, f)
        return True
    except FileNotFoundError:
        print("{} not found.".format(csv_filename))
        return False
    except csv.Error as e:
        print("Error reading CSV: {e}".format(e))
        return False
    except Exception as e:
        print("Unexpected error: {e}".format(e))
        return False
