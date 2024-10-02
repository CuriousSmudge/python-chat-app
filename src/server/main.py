from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/user/profile-<userID>")
def hello_world(userID):
    return f"here is the data for {userID}: \n blah blah"

@app.route("/user/create", methods=["POST"])
def create_user():
    data = request.json
    print(data)
    
    if data is None or data == "":
        return 'bad request!', 400

    try:
        username = data["username"]
        password_hash = data["password_hash"]
    except KeyError:
        return f"missing field {KeyError}", 400

    return str()
