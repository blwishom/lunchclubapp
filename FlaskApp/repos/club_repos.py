from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError, Regexp, Length
from .db import db
from datetime import datetime
from sqlalchemy import UniqueConstraint

class Club(db.Model):
    __tablename__ = 'clubs'
    __table_args__ = (UniqueConstraint(
        'name', name='uq_clubs_name'),)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    location = db.Column(db.String(255), nullable=False)
    join_code = db.Column(db.String(6), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location
        }

'''
id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(255), nullable=False, unique=True)
location = db.Column(db.String(255), nullable=False)
join_code = db.Column(db.String(6), nullable=False)
created_at = db.Column(db.DateTime, default=datetime.utcnow)
updated_at = db.Column(db.DateTime, default=datetime.utcnow)
'''

def club_exists(form, field):
    # Checking if club exists
    name = field.data
    club = Club.query.filter(Club.name == name).first()
    if club is not None:
        raise ValidationError(f"'{name}' is already the name of a club. Try another name")


class ClubForm(FlaskForm):
    name = StringField('Club Name:', validators=[DataRequired(), club_exists, Length(min=3, max=255, message="Name must be between 5 and 50 characters.")])
    location = StringField('Location:', validators=[DataRequired(), Length(min=3, max=255, message="Location must be 3 characters or longer.")])
    join_code = StringField(validators=[Regexp('^\d{6}$', message="Join code must be 6 digits of numbers.")])

    class Meta: # for testing purposes only. Need to reenable csrf for production
        csrf = False

class EditClubForm(FlaskForm):
    name = StringField('Club Name:', validators=[DataRequired(), Length(min=3, max=255, message="Name must be between 5 and 50 characters.")])
    location = StringField('Location:', validators=[DataRequired(), Length(min=3, max=255, message="Location must be 3 characters or longer.")])
    join_code = StringField(validators=[Regexp('^\d{6}$', message="Join code must be 6 digits of numbers.")])
    
    def validate_name(self, field):
        club = Club.query.filter_by(name=field.data).first()
        # print(f"self.id is {self.id}")
        if club is not None and club.id != self.id:
            raise ValidationError(f"'{field.data}' is already the name of a club. Try another name")

    class Meta: # for testing purposes only. Need to reenable csrf for production
        csrf = False