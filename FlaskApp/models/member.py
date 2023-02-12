from .db import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Enum, UniqueConstraint

member_type = Enum('banned', 'regular', 'admin', name='member_type')

class Member(db.Model, UserMixin):
    __tablename__ = 'members'
    __table_args__ = (UniqueConstraint('username', name='uq_members_username'),)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    club_id = db.Column(db.Integer)
    member_info = db.Column( member_type)
    last_login = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    password_digest = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @property
    def password(self):
        return self.password_digest

    @password.setter
    def password(self, password):
        self.password_digest = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'club_id': self.club_id,
            'member_info': self.member_info,
            'last_login': self.last_login
        }
