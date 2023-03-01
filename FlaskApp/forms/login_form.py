from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from models import Member


def member_exists(form, field):
    # Checking if user exists
    email = field.data
    member = Member.query.filter(Member.email == email).first()
    if not member:
        raise ValidationError('Email provided not found.')


def password_matches(form, field):
    # Checking if password matches
    password = field.data
    email = form.data['email']
    member = Member.query.filter(Member.email == email).first()
    if not member:
        raise ValidationError('No such member exists.')
    if not member.check_password(password):
        raise ValidationError('Password was incorrect.')

        
class LoginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), member_exists])
    password = StringField('password', validators=[
                           DataRequired(), password_matches])
