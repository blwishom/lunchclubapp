from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, ValidationError, Regexp, Length
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
    # Checking if club exists
    name = field.data
    club = Club.query.filter(Club.name == name).first()
    if club is not None:
        raise ValidationError(f"'{name}' is already the name of a club. Try another name")


# def joincode_matches(form, field):
#     # Checking if password matches
#     join_code = field.data
#     name = form.data['name']
#     club = Club.query.filter(Club.join_code == join_code).first()
#     if not club:
#         raise ValidationError('No such club exists.')

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

    # def set_data(self, club):
    #     self.name.data = club.name
    #     self.location.data = club.location
    #     self.join_code.data = club.join_code
    
    def validate_name(self, field):
        club = Club.query.filter_by(name=field.data).first()
        # print(f"self.id is {self.id}")
        if club is not None and club.id != self.id:
            raise ValidationError(f"'{field.data}' is already the name of a club. Try another name")

    class Meta: # for testing purposes only. Need to reenable csrf for production
        csrf = False