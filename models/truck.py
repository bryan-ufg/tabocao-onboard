from db import db
from datetime import datetime, timezone

class TruckModel(db.Model):
    __tablename__ = "trucks"

    id = db.Column(db.Integer, primary_key=True)
    alias = db.Column(db.String)
    model = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    license_plate = db.Column(db.String, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False)

    trips = db.relationship("TripModel", back_populates=__tablename__, cascade="all, delete-orphan")
    truck_maintenance = db.relationship("TruckMaintenanceModel", back_populates=__tablename__, cascade="all, delete-orphan")