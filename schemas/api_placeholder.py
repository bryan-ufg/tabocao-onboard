from marshmallow import Schema, fields

class APIPlaceholderSchema(Schema):
    id = fields.Int(dump_only=True)
    content = fields.Dict(required=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)