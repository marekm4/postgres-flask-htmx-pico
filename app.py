import os

import psycopg
from flask import Flask, render_template, request

from register import get_users, add_user

app = Flask(__name__)
db = psycopg.Connection.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    dbname=os.getenv('DB_NAME'),
)
db.autocommit = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        add_user(db, request.form["name"])
    return render_template("register.html", users=get_users(db))
