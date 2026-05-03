from config import db
from geoalchemy2 import Geography
from geoalchemy2.shape import from_shape, to_shape
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(50), unique=True, nullale=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    vibes = db.relationship("Vibe", backref="author", lazy=True)


class Vibe(db.Model):
    __tablename__ = "vibes"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"), nullable=False)
    content = db.Column(db.string(500), nullable=False)
    is_active = db.Column(db.boolean, default=True)
    is_public = db.Column(db.boolean,default=True)
    location = db.Column(Geography(geometry_type="POINT", srid=4326, nullable=False))
    created_at = db.Column(db.DateTime, default=datetime.now)
