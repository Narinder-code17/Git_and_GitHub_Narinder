from flask import Flask, jsonify, render_template, request
import json
import os
from pymongo import MongoClient
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

db = client["git_github_db"]
todo_collection = db["todo_items"]


@app.route("/")
def home():
    return "Flask application is running successfully."


@app.route("/api")
def api():
    with open("data.json", "r") as file:
        data = json.load(file)

    return jsonify(data)

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    item_name = request.form.get("itemName")
    item_description = request.form.get("itemDescription")

    if not item_name or not item_description:
        return jsonify({
            "error": "itemName and itemDescription are required"
        }), 400

    result = todo_collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return jsonify({
        "message": "To-Do item submitted successfully",
        "itemId": str(result.inserted_id)
    }), 201
    
if __name__ == "__main__":
    app.run(debug=True)