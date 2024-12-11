from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

QUIZ_SERVICE = "http://localhost:5001"
RESULT_SERVICE = "http://localhost:5002"

@app.route("/quiz/<planet>")
def quiz(planet):
    # Proxy request to Quiz Service
    response = requests.get(f"{QUIZ_SERVICE}/quiz/{planet}")
    return response.content

@app.route("/result", methods=["POST"])
def result():
    # Proxy request to Result Service
    response = requests.post(f"{RESULT_SERVICE}/result", json=request.json)
    return response.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
