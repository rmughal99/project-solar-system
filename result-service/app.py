from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/result", methods=["POST"])
def result():
    # Dummy result evaluation logic
    data = request.json
    score = len(data.get("answers", []))  # Example logic
    return jsonify({"score": score})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
