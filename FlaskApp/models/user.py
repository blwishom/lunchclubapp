from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


<<<<<<< HEAD
class User(db.Model, UserMixin):
=======
class Member(db.Model, UserMixin):
>>>>>>> 4e8d59e094db1e9968185ffee658e1d607510219
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    club_id = db.Column(db.Integer)
    hashed_password = db.Column(db.String(50), nullable=False)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username,
            'email': self.email,
            'club_id': self.club_id
        }
