from flask import Blueprint, render_template

blp = Blueprint("main", __name__)

@blp.route("/")
def index():
    return render_template("index.html")
