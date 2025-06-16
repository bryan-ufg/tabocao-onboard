from marshmallow import Schema, fields

from schemas import TruckSchema

class TruckMaintenanceSchema(Schema):
    id = fields.Int(dump_only=True)

    truck_id = fields.Int(required=True)
    truck = fields.Nested(TruckSchema, dump_only=True)

    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    location = fields.Str()
    description = fields.Str()

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)