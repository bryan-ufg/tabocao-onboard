from marshmallow import Schema, fields

from schemas import DriverSchema

class ASOSchema(Schema):
    id = fields.Int(dump_only=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    description = fields.Str()
    analyst = fields.Str()

    driver_id = fields.Int(required=True)
    driver = fields.Nested(DriverSchema, dump_only=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)