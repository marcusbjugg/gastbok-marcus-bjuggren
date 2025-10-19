from flask import Flask, render_template, request, redirect
import json
from datetime import datetime
import os

app = Flask(__name__)

JSON_FILE = "gästbok.json" 

def ladda_posts():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def spara_posts(posts):
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

@app.route("/")
def index():
    posts = ladda_posts()
    posts.reverse()
    return render_template("index.html", posts=posts)

@app.route("/tillägg", methods=["POST"])
def lägg_till():
    namn = request.form.get("namn")
    email = request.form.get("email")
    kommentar = request.form.get("kommentar")
    tid = datetime.now().strftime("%Y-%m-%d %H:%M")

    ny_post = {
        "namn": namn,
        "email": email,
        "kommentar": kommentar,
        "tid": tid
    }

    posts = ladda_posts()
    posts.append(ny_post)
    spara_posts(posts)
    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')