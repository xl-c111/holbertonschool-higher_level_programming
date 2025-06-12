#!/usr/bin/python3
from flask import Flask, jsonify, request

# Initialize Flask app
app = Flask(__name__)
users = {}


# Homepage welcome endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# Get all usernames endpoint
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))


# Status check endpoint
@app.route("/status")
def get_status():
    return "OK"


# Get single user endpoint
@app.route("/users/<username>")
def get_username_obj(username):
    if username in users:
        return jsonify(users[username]), 200
    else:
        return jsonify({"error": "User not found"}), 404


# Add user (POST) endpoint
@app.route("/add_user", methods=['POST'])
def add_user():
    # get JSON data sent with the POST request
    data = request.get_json()
    # return 400 if no data is sent
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    # get username value from data dict
    username = data.get("username")
    # check if username is missing or empty
    if not username:
        return jsonify({"error": "Username is required"}), 400
    # add the new user data to users dict using username as key
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
