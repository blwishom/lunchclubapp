from .db import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Enum, UniqueConstraint

member_type = Enum('banned', 'regular', 'admin', name='member_type')

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    __table_args__ = (UniqueConstraint(
        'name', name='uq_restaurants_name'),)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # @property
    # def password(self):
    #     return self.password_digest

    # @password.setter
    # def password(self, password):
    #     self.password_digest = generate_password_hash(password)

    # def check_password(self, password):
    #     return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
        }
