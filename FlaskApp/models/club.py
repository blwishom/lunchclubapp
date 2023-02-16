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

    def validate(self):
        if len(self.name) < 3:
            raise ValueError('Name must be at least 3 characters long')
        if len(self.location) < 2:
            raise ValueError('Location must be at least 2 characters long')
        if len(self.join_code) != 6:
            raise ValueError('Join code must be 6 characters long')
            
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location
        }
