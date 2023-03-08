from .db import db
from datetime import datetime


class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    __table_args__ = (db.UniqueConstraint('name', 'address', name='_name_address_uc'),)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
        }
