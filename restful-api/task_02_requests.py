#!/usr/bin/python3

import requests
import csv

response = requests.get("https://jsonplaceholder.typicode.com/posts")


def fetch_and_print_posts():

    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        response_dict = response.json()
        for post in response_dict:
            print(post["title"])


def fetch_and_save_posts():

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
