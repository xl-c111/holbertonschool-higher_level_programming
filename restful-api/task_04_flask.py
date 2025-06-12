#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    return "OK"


@app.route("/users/<username>")
def get_username_obj(username):
    if username in users:
        return jsonify(users[username]), 200
    else:
        return jsonify({"error": "User not found"}), 404


# specify only POST method is allowed
@app.route("/add_user", methods=['POST'])
def add_user():
    # get JSON data sent with the POST request
    data = request.get_json()
    # check if no data sent
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    # get username value from data dict
    username = data.get("username")
    # check if username is missing or empty
    if not username:
        return jsonify({"error": "Username is required"}), 400
    # add the user data to users dict using username as key
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
