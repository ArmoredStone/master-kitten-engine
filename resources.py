from flask import Blueprint, request, jsonify, render_template, abort, send_from_directory
from schemas import OrderSchema

from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from models import OrderModel
from db import db

order_schema = OrderSchema()
blp = Blueprint("main", __name__)

@blp.route("/")
def index():
    return render_template("index.html")

@blp.route("/static/pictures/master-kitten-engine.png")
def logo():
    return send_from_directory('static/pictures', 'master-kitten-engine.png')

@blp.route("/send_order", methods=['POST'])
def create_order():
    data = request.get_json()
    
    errors = order_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    
    validated_data = order_schema.load(data)
    
    email = validated_data.get('email')
    quantity = validated_data.get('quantity')
    
    new_order = OrderModel(email=email, quantity=quantity)
    
    try:
        db.session.add(new_order)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        abort(500, message=str(e))
    
    result = order_schema.dump(new_order)
    print(result)
    
    return jsonify({'message': 'Order created successfully!', 'order': result}), 201
