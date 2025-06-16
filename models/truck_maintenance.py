from db import db
from datetime import datetime, timezone

class TruckMaintenanceModel(db.Model):
    __tablename__ = "truck_maintenance"

    id = db.Column(db.Integer, primary_key=True)

    truck_id = db.Column(db.Integer, db.ForeignKey('trucks.id'), nullable=False)
    trucks = db.relationship("TruckModel", back_populates=__tablename__)

    start_date = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    end_date = db.Column(db.DateTime(timezone=True), nullable=False)
    location = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False)