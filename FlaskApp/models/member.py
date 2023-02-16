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

    def validate(self):
        import re
        if self.username is None or len(self.username) < 3:
            raise ValueError('Username must be at least 3 characters long')
        if self.name is None or len(self.name) < 3:
            raise ValueError('Name must be at least 3 characters long')
        if self.email is None or re.search(r"^[A-Za-z]+[A-Za-z0-9._\-]*@[a-z][a-z0-9.-]*\.[a-z]{2,}$", self.email) is None:
            raise ValueError('Email must be valid')
        if self.member_info is None or self.member_info not in ['banned', 'regular', 'admin']:
            raise ValueError('Member must be either banned, regular, or admin')
        if self.club_id is None:
            raise ValueError('Member must be associated with a club')

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
