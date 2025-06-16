from db import db
from datetime import datetime, timezone

class DriverModel(db.Model):
    __tablename__ = "drivers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    cpf = db.Column(db.String, unique=True, nullable=False)
    driver_license = db.Column(db.String, unique=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False)

    trips = db.relationship("TripModel", back_populates=__tablename__, cascade="all, delete-orphan")