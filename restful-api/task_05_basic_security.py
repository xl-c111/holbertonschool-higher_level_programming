#!/usr/bin/python3

# Flask creates the web app
# jsonify formats response as JSON
# request handles incoming HTTP request data
from flask import Flask, jsonify, request
# import HTTPBasicAuth class, which enables HTTP Basic Authentication
from flask_httpauth import HTTPBasicAuth
# generate_password_hash hashes a password for secure storage
# check_password_hash checks password against its hash
from werkzeug.security import generate_password_hash, check_password_hash
# create_access_token/create_refresh_token for creating tokens
# get_jwt_identity/get_jwt to extract identities and claims
# jwt_required decorator to protect routes
# JWTManager to initialize JWT extension
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required, get_jwt, JWTManager


app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    user_info = users.get(username)
    if user_info and check_password_hash(user_info["password"], password):
        return user_info
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    # extract credentials
    username = data.get("username")
    password = data.get("password")
    user_info = users.get(username)

    if user_info and check_password_hash(user_info["password"], password):
        additional_claims = {"role": user_info["role"]}
        access_token = create_access_token(
            identity=username, additional_claims=additional_claims)
        # package token into a dict, using jsonify convert it to JSON and then return it as HTTP reponse back to client
        return jsonify({"access_token": access_token})
    return jsonify({'error': 'Invalid credentials'}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    # retrieve all claims from the JWT token
    claims = get_jwt()
    # check if the user's role in claims is not admin; deny access if not
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()


# Workflow
"""
1, Initialize Flask obj app and authentication tools
   - app = Flask(__name__): create a Flask app obj, __name__ tells Flask where to look for resources
   - auth = HTTPBasicAuth(): create an obj of HTTPBasicAuth class to manage authentication
   - app.config["JWT_SECRET_KEY"] = "super-secret": set a secret key for JWT signing and verification
   - jwt = JWTManager(app): create a JWTManager obj to enable JWT support in the Flask app

2, set up a method to check the user's password
   - @auth.verify_password: register a function to check username and password
   - user_info = users.get(username): look up the user info in the users dict using username as key, 
                                      it will return a user info dict
   - if user_info: if user info exists
   - check_password_hash(user_info["password"], password): to check if the hashed password stored in 
                            user_info["password"] matches the plain-text password provided by client

3, Support two types of login - Basic Authentication (providing username and password each time)
   Design two separate protected endpoints - Protect endpoint with Basic Authentication
   - @app.route("/basic-protected", methods=["GET"]): define a route /basic-protected using GET
   - @auth.login_required: decorator enforces Basic Auth protection(only clients who provide a valid
                           username and password can access this endpoint)

4, Support two types of login - JWT authentication(you log in once, and the server issues you a "token", 
                                by presenting this token, without needing to enter your username and password every time)
   - @app.route("/login", methods=["POST"]): define a route /login using POST
   - data = request.get_json(): get login information by retrieving JSON data from request
   - username = data.get("username"): using get() method to retrieve the value of the key "username"
   - user_info = users.get(username): then look up the user information in your users dictionary using 
                                      the username, returns the user info dict if found.
   - verify user and password
   - additional_claims = {"role": user_info["role"]}: create a new dict containing user's role, 
                    used as extra claim when generating JWT token
   - access_token = create_access_token(identity=username, additional_claims=additional_claims): create a
                    JWT token, set identity as username, and attach additional claims
   - return jsonify({"access_token": access_token}): package token into a dict, using jsonify convert
                    it to JSON and then return it as HTTP reponse back to client

5, Design two separate protected endpoints - Protect endpoint with JWT
   - @app.route("/jwt-protected"): define a route using GET 
   - @jwt_required(): decorator enforces JWT protection(only requests with a valid JWT access token can access)

6, Design an endpoint specifically for admin
   - claims = get_jwt(): when a request with a valid JWT token coming in, Flask-JWT-Extended decodes the
                        token and makes its payload(claims) available via get_jwt(), claims dict contains
                        all the fields in the token.
   - if claims.get("role") != "admin": retrieve the value associated with the key 'role' in the claims dict. 

7, Unified authentication error handling
"""
