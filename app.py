from flask import Flask, render_template, request

from db import get_db, get_users, add_user

app = Flask(__name__)
db = get_db()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        add_user(db, request.form["name"])
    return render_template("register.html", users=get_users(db))
