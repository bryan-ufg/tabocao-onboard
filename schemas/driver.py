from marshmallow import Schema, fields, validate
from datetime import datetime, timezone

class DriverSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    birthday = fields.Date(required=True, format='%Y-%m-%d')
    cpf = fields.Str(required=True, validate=validate.Regexp(r'^\d{11}$'))
    driver_license = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)