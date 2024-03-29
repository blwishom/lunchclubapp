from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Email, ValidationError, Regexp, Length, Optional
from models import Member, Club, User
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

# class MockObject:
#     def __init__(self, **kwargs):
#         self.name = kwargs.get("name")
#         self.id = kwargs["id"]
#         self.username = kwargs.get("username")

# fake_objs = [MockObject(name=f"Name {i}", id=i, username=f"User{1}") for i in range(1, 3)]

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