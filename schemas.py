from marshmallow import Schema, fields

class PlainOrderSchema(Schema):
    id = fields.Int(dump_only=True)

class OrderSchema(PlainOrderSchema):
    email = fields.Str(required=True)
    quantity = fields.Int(required=True)
