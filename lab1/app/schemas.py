from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    currency_id = fields.Int(required=False)


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    sum = fields.Float(required=True)
    currency_id = fields.Int(required=False)


class CurrencySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
