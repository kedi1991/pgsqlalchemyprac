from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/newtask")
def newtask():
    return render_template("newtask.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")
