from extensions import db
from datetime import datetime, timezone

class TripModel(db.Model):
    __tablename__ = "trips"

    id = db.Column(db.Integer, primary_key=True)
    start_city = db.Column(db.String, nullable=False)
    end_city = db.Column(db.String, nullable=False)
    start_date = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    end_date = db.Column(db.DateTime(timezone=True), nullable=False)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False)

    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'), nullable=False)
    drivers = db.relationship("DriverModel", back_populates=__tablename__)

    truck_id = db.Column(db.Integer, db.ForeignKey('trucks.id'), nullable=False)
    trucks = db.relationship("TruckModel", back_populates=__tablename__)