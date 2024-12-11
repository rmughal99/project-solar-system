from flask import Flask, render_template

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/quiz/<planet>")
def quiz(planet):
    # Render quiz page based on the planet
    return render_template(f"{planet}.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
