from db import db

class OrderModel(db.Model):
    __tablename__ = "orders"
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, db.CheckConstraint("email LIKE '%@%'"))
    quantity = db.Column(db.Integer, db.CheckConstraint("quantity > 0 AND quantity <= 100"))
