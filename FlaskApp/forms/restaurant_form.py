from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email, ValidationError, Length
from models import Restaurant

'''
id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(255), nullable=False)
address = db.Column(db.String(255), nullable=False)
created_at = db.Column(db.DateTime, default=datetime.utcnow)
updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
'''

def restaurant_exists(form, field):
    # Checking if restaurant exists
    name = field.data
    address = form.data['address']
    restaurant = Restaurant.query.filter(Restaurant.name == name).first()
    if restaurant is not None and restaurant.address == address:
        raise ValidationError(f"'{field.data}' at {address} is already an existing restaurant.")

class RestaurantForm(FlaskForm):
    name = StringField('Restaurant: ', validators=[DataRequired(), restaurant_exists, Length(min=5, max=255, message="Name must be between 5 and 255 characters.")])
    address = StringField('Address: ', validators=[DataRequired(), Length(min=5, max=255, message="Address must be between 5 and 255 characters.")])

    class Meta:
        csrf = False

class EditRestaurantForm(FlaskForm):
    name = StringField('Restaurant: ', validators=[DataRequired(), Length(min=5, max=255, message="Name must be between 5 and 255 characters.")])
    address = StringField('Address: ', validators=[DataRequired(), Length(min=5, max=255, message="Address must be between 5 and 255 characters.")])
    
    def validate_name(self, field):
        restaurant = Restaurant.query.filter_by(address=self.address.data).first()
        
        if restaurant is not None and restaurant.id != self.id and restaurant.name == field.data:
            raise ValidationError(f"'{field.data}' at {restaurant.address} is already the name and address of an existing restaurant.")

    class Meta:
        csrf = False