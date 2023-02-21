from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from models import Club

'''
id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(255), nullable=False, unique=True)
location = db.Column(db.String(255), nullable=False)
join_code = db.Column(db.String(6), nullable=False)
created_at = db.Column(db.DateTime, default=datetime.utcnow)
updated_at = db.Column(db.DateTime, default=datetime.utcnow)
'''

def club_exists(form, field):
    # Checking if user exists
    email = field.data
    club = Club.query.filter(Club.email == email).first()
    if not club:
        raise ValidationError('The email provided was not found.')


def joincode_matches(form, field):
    # Checking if password matches
    join_code = field.data
    name = form.data['name']
    club = Club.query.filter(Club.join_code == join_code).first()
    if not club:
        raise ValidationError('No such club exists.')
    if not club.check_password(join_code):
        raise ValidationError('Password entered was incorrect.')


class ClubForm(FlaskForm):
    name = StringField('Club Name: ', validators=DataRequired(), club_exists, validators=[Length(min=3, max=255, message="Name must be between 5 and 50 characters.")])
    location = StringField('Location: ', validators=DataRequired(), club_exists, validators=[Length(min=3, max=255, message="Location must be 3 characters or longer.")])
    join_code = IntegerField(validators=[NumberRange(min=6, max=6, message="Join code must be 6 digits of numbers.")])
