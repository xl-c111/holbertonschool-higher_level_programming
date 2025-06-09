#!/usr/bin/env python3
"""This module demonstrates how to fetch post data from a RESTful API using
the `requests` library and save the data into a CSV file using Python's `csv`
module"""
import requests
import csv

response = requests.get("https://jsonplaceholder.typicode.com/posts")


def fetch_and_print_posts():
    """
    Print the status code and the title of each post fetched from the API.
    """
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        response_dict = response.json()
        for post in response_dict:
            print(post["title"])


def fetch_and_save_posts():
    """
    Fetch posts from the API and save them into a CSV file called 'posts.csv'
    The CSV file will have columns: id, title, body.
    """
    if response.status_code == 200:

        response_dict = response.json()
        new_dict = []

        for post in response_dict:
            new_dict.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

    with open("posts.csv", "w", newline="", encoding="utf-8") as f:
        csv_writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
        csv_writer.writeheader()
        csv_writer.writerows(new_dict)
