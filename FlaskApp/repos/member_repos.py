from .db import db
from datetime import datetime
from sqlalchemy import Enum
from sqlalchemy.orm import relationship
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Email, ValidationError, Length, Optional
from repos import Club, User

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

'''
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
'''

def email_exists(form, field):
    # Checking if email exists
    email = field.data
    member = Member.query.filter(Member.email == email).first()
    if member is not None:
        raise ValidationError(f"{email} is already registered. Use another email")
    
def user_already_linked(form, field):
    user_id = field.data
    user = User.query.filter(User.id == user_id).first()
    if user.members is not None:
        raise ValidationError(f"This user is already attached to {user.members.email}. Use another username")

class MemberForm(FlaskForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.club_id.choices = [(club.id, club.name) for club in Club.query.all()]
        self.user_id.choices = [(user.id, user.username) for user in User.query.all()]

    name = StringField('Member Name:', validators=[DataRequired(), Length(min=5, max=50, message="Name must be between 5 and 50 characters.")])
    member_info = SelectField("Member Type: ", choices=[('banned', 'Banned'), ('regular', 'Regular'), ('admin', 'Admin')], validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired(), email_exists, Email()])

    club_id = SelectField('Club: ', coerce=int, validators=[DataRequired()])

    user_id = SelectField('User: ', coerce=int, validators=[Optional(), user_already_linked])

    class Meta: # for testing purposes only. Need to reenable csrf for production
        csrf = False

class EditMemberForm(FlaskForm):

    name = StringField('Member Name:', validators=[DataRequired(), Length(min=5, max=50, message="Name must be between 5 and 50 characters.")])
    member_info = SelectField("Member Type: ", choices=[('banned', 'Banned'), ('regular', 'Regular'), ('admin', 'Admin')], validators=[DataRequired()])
    email = StringField('Email: ', validators=[DataRequired(), Email()])
    
    def validate_email(self, field):
        member = Member.query.filter_by(email=field.data).first()
        if member is not None and member.id != self.id:
            raise ValidationError(f"{field.data} is already registered. Use another email")

    class Meta: # for testing purposes only. Need to reenable csrf for production
        csrf = False