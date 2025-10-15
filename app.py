from flask import Flask, render_template
import json

app = Flask(__name__)

JSON_FILE = "gästbok.json" 

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')