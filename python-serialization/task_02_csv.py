#!/usr/bin/python3
"""This module provides a function to convert CSV files to JSON format."""
import csv
import json


def convert_csv_to_json(csv_filename):
    """ Convert a CSV file to JSON format."""
    with open("data.csv", "r", newline="") as f:

        reader = csv.DictReader(f)
        for row in reader:
            print(row)
