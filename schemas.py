from marshmallow import Schema, fields

class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(required=True)
    quantity = fields.Int(required=True)
