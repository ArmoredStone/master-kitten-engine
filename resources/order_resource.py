from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import OrderModel
from schemas import OrderSchema

blp = Blueprint(OrderModel.__tablename__, "order")
