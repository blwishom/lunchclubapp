from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from models import Member


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


class SignUpForm(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired(), username_exists])
    email = StringField('email', validators=[DataRequired(), member_exists])
    password = StringField('password', validators=[DataRequired()])
