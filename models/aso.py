from extensions import db
from datetime import datetime, timezone

class ASOModel(db.Model):
    __tablename__ = "aso"

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    end_date = db.Column(db.DateTime(timezone=True), nullable=False)
    description = db.Column(db.String, nullable=False)
    analyst = db.Column(db.String(100), nullable=False)

    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'), nullable=False)
    drivers = db.relationship("DriverModel", back_populates=__tablename__)

    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False)