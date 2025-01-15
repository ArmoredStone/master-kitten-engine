from schemas import OrderSchema
from models import OrderModel
from db import db

from flask import Blueprint, request, jsonify, render_template, abort, send_from_directory
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError

blp = Blueprint("main", __name__)

@blp.route("/")
def index():
    return render_template("index.html")

@blp.route("/static/pictures/master-kitten-engine.png")
def logo():
    return send_from_directory('static/pictures', 'master-kitten-engine.png')

@blp.route("/send_order", methods=['POST'])
def create_order():
    try:
        # Get data from the form
        email = request.form["email"]
        quantity = int(request.form["quantity"])
        # Validate the data using the Marshmallow schema
        OrderSchema().load({"email": email, "quantity": quantity})
    except ValidationError as err:
        print(err)
        abort(400)
    except (KeyError, ValueError):
        abort(400)
    
    new_order = OrderModel(email=email, quantity=quantity)
    
    try:
        db.session.add(new_order)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        abort(500, message=str(e))
    
    return render_template("response.j2", success=True, email=new_order.email, quantity=new_order.quantity)
