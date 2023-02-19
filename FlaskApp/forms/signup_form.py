from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, ValidationError, Length
from models import Member, Club

"""
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
"""


def member_exists(form, field):
    # Checking if user exists
    email = field.data
    member = Member.query.filter(Member.email == email).first()
    if member:
        raise ValidationError('Email address is already in use.')


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    member = Member.query.filter(Member.username == username).first()
    if member:
        raise ValidationError('Username is already in use.')

def club_exists(form, field):
    # Checking if club exists
    if field.data is not None:
        club_id = field.data
        club = Club.query.filter(Club.id == club_id).first()
        if club is None:
            raise ValidationError('Club does not exist.')

class SignUpForm(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired(), username_exists, Length(min=3, max=20)])
    email = StringField('email', validators=[DataRequired(), Email(), member_exists])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6)])
    club_id = IntegerField('club_id', validators=[club_exists])
    member_info = SelectField('member_info', choices=[('regular', 'regular'), ('admin', 'admin'), ('banned', 'banned')], validators=[DataRequired()])