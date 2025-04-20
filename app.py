from flask import Flask, render_template, request

from db import get_db, get_users, add_user

app = Flask(__name__)
db = get_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    errors = []
    if request.method == "POST":
        name = request.form.get("name")
        if len(name) > 0:
            add_user(db, name)
        else:
            errors.append("Name is required")
    return render_template("register.html", errors=errors, users=get_users(db))
