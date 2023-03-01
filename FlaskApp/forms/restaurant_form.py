from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError
from models import Restaurant

'''
id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(255), nullable=False)
address = db.Column(db.String(255), nullable=False, unique=True)
created_at = db.Column(db.DateTime, default=datetime.utcnow)
updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
'''

def restraurant_exists(form, field):
    # Checking if restaurant exists
    name = field.data
    restaurant = Restaurant.query.filter(Restaurant.name == name).first()
    if not restaurant:
        raise ValidationError('The email provided was not found.')


class RestaurantForm(FlaskForm):
    name = StringField('Restaurant: ', validators=DataRequired(), club_exists, validators=[Length(min=5, max=255, message="Name must be between 5 and 255 characters.")])
    address = StringField('Address: ', validators=DataRequired(), club_exists, validators=[Length(min=5, max=255, message="Address must be betwen 5 and 255 characters.")])
