from flask import Flask

from db import db
from resources import blp as MainBlueprint

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    app.register_blueprint(MainBlueprint)

    with app.app_context():
        db.create_all()

    return app
