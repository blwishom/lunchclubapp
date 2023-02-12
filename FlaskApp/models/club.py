from .db import db
from datetime import datetime
from sqlalchemy import UniqueConstraint

class Club(db.Model):
    __tablename__ = 'clubs'
    __table_args__ = (UniqueConstraint(
        'name', name='uq_clubs_name'),)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    location = db.Column(db.String(255), nullable=False)
    join_code = db.Column(db.String(6), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location
        }
