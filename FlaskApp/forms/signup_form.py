from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, ValidationError, Length
from models import User, Club


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError('Username is already in use.')

class SignUpForm(FlaskForm):
    username = StringField(
        'username', validators=[DataRequired(), username_exists, Length(min=3, max=20)])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6)])

    class Meta: # for testing purposes only. Need to reenable csrf for production
        csrf = False
