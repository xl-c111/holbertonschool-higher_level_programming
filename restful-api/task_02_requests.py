#!/usr/bin/python3

import requests
import csv

# send a GET request to the given URL and store the result in the response obj
response = requests.get("https://jsonplaceholder.typicode.com/posts")


def fetch_and_print_posts():

    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        # convert JSON response to python obj, typeof(posts): list[dict]
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():

    if response.status_code == 200:
        posts = response.json()
        new_dict = []

        for post in posts:
            # loop through each post, extracts three fields from each post
            # construct a new dict with 3 fields and append it to the list new_dict
            new_dict.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

    # open a file named 'posts.csv' in write mode suing with()
    with open("posts.csv", "w", newline="", encoding="utf-8") as f:
        # Use csv.DictWriter() to create a writer obj, specifying the fields name
        csv_writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
        # write the header(field name)
        csv_writer.writeheader()
        # write all the post data
        csv_writer.writerows(new_dict)


# Workflow
"""
1, send GET request
   - Syntax: response = request.GET(URL) (data retrieved from URL are JSON strings)

2, check status code
   - if response.status_code == 200

3, parse JSON data
   - posts = response.JSON(): convert JSON data to a poython obj(dict or list)
   - posts are usually list of dicts [{}, {}, ...]

4, loop through the list and print titles
  - for post in posts: post["key"] gets the value of the given key

5, extract the useful fields and construct a new list of dicts
  - create an empty new list []
  - loop through posts, extract the useful fields and construct a new list of dicts
    new_list = [{"id": posts["id"], "title": post["title"], "body": posts["body"}]

6, write the simplified data to CSV file
  - use csv.DictWriter() create a new writer obj, specifying the fields names
  - writer_obj.writeheader() writes the header
  - writer_obj.writerows(simplified data) writes all the posts data 
"""
