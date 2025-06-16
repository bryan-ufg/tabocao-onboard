from marshmallow import Schema, fields

from schemas import DriverSchema
from schemas import TruckSchema

class TripSchema(Schema):
    id = fields.Int(dump_only=True)
    start_city = fields.Str(required=True)
    end_city = fields.Str(required=True)
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    description = fields.Str()

    driver_id = fields.Int(required=True)
    driver = fields.Nested(DriverSchema, dump_only=True)

    truck_id = fields.Int(required=True)
    truck = fields.Nested(TruckSchema, dump_only=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)