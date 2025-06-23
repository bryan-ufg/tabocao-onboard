from db import db
from datetime import datetime, timezone

class APIPlaceholderModel(db.Model):
    __tablename__ = "api_placeholder"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.JSON, nullable=False)

    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=False)