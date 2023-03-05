from .db import db
from datetime import datetime
from sqlalchemy import Enum
from sqlalchemy.orm import relationship

member_type = Enum('banned', 'regular', 'admin', name='member_type')

class Member(db.Model):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    club_id = db.Column(db.Integer, db.ForeignKey('clubs.id'))
    member_info = db.Column( member_type)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = relationship("User", back_populates="members")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'club_id': self.club_id,
            'member_info': self.member_info,
            'user_id': self.user_id
        }
