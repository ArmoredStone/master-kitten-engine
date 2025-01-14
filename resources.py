from flask import Blueprint, render_template, abort
from schemas import OrderSchema

from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError

from models import OrderModel
from db import db

blp = Blueprint("main", __name__)

@blp.route("/")
def index():
    return render_template("index.html")

@blp.route("/send_order")
class Order(MethodView):
    @blp.arguments(OrderSchema)
    @blp.response(201, OrderSchema)
    def post(self, order_data):
        order = OrderModel(**order_data)
        try:
            db.session.add(order)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500, message=str(e))
        return order
