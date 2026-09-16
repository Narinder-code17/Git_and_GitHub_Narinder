from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)


@app.route("/")
def home():
    return "Flask application is running successfully."


@app.route("/api")
def api():
    with open("data.json", "r") as file:
        data = json.load(file)

    return jsonify(data)

@app.route("/todo")
def todo():
    return render_template("todo.html")
    
if __name__ == "__main__":
    app.run(debug=True)