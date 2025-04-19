from flask import Flask, render_template, request

from todo import get_tasks, add_task

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/todo", methods=["GET", "POST"])
def todo():
    if request.method == "POST":
        add_task(request.form["task"])
    return render_template("todo.html", tasks=get_tasks())
