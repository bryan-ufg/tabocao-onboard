from marshmallow import Schema, fields, validate
from datetime import datetime, timezone

class TruckSchema(Schema):
    id = fields.Int(dump_only=True)
    alias = fields.Str()
    model = fields.Str(required=True)
    year = fields.Int(required=True)
    license_plate = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)