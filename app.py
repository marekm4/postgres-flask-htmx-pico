import os

import psycopg
from flask import Flask, render_template, request

from todo import get_tasks, add_task

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


@app.route("/todo", methods=["GET", "POST"])
def todo():
    if request.method == "POST":
        add_task(db, request.form["task"])
    return render_template("todo.html", tasks=get_tasks(db))
