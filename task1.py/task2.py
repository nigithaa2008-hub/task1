from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
users_collection = db["users"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    data = request.json

    if not data:
        return jsonify({"message": "No data received"})

    name = data.get("name", "")
    password = data.get("password", "")

    if not name.isalpha():
        return jsonify({"message": "Name should contain only letters"})

    if not password.isdigit():
        return jsonify({"message": "Password should contain only numbers"})

    users_collection.insert_one({
        "name": name,
        "password": password
    })

    return jsonify({"message": "Registered Successfully"})

if __name__ == "__main__":
    app.run(debug=True)