from flask import render_template, request, url_for, redirect
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
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/addcategory", methods=['GET', 'POST'])
def addcategory():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("addcategory.html")


@app.route("/editcategory/<int:category_id>", methods=['GET','POST'])
def editcategory(category_id):
    if request.method =="POST":
        category = Category.query.get_or_404(category_id)
       
        return render_template("editcategory.html")
    return render_template("editcategory.html")