from models import Member, db
from sqlalchemy.exc import SQLAlchemyError
from flask import abort
from forms import MemberForm, EditMemberForm
from wtforms import ValidationError

def get_members():
    members = Member.query.all()
    return members

def create_member(**member_data):
    try:
        # call validations referencing other tables
        form = MemberForm(**member_data)
    except ValidationError as e:
        return str(e)
    if form.validate_on_submit():
        new_member = Member(**member_data)
        try:
            db.session.add(new_member)
            db.session.commit() # if this fails then connection to database is not closed
            return new_member.to_dict()
        except SQLAlchemyError as e:
            return {'SQL error': str(e)}
    else:
        return { 'errors': str(form.errors)}, 400

def get_member(id):
    member = Member.query.get_or_404(id)
    if (member is None):
        abort(404)
    return member.to_dict()

def update_member(id, **member_data):
    member = Member.query.get_or_404(id)
    if (member is None):
        abort(404)
    try:
        form = EditMemberForm(obj=member)
        form.id = member.id
    except ValidationError as e:
        return str(e)

    if form.validate_on_submit():
        form.populate_obj(member)
        try:
            db.session.commit() # if this fails then connection to database is not closed
            return member.to_dict()
        except SQLAlchemyError as e:
            return {'SQL error': str(e)}
    else:
        return {'errors': str(form.errors)}, 400
