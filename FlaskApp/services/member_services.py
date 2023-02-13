from models import Member, db
from sqlalchemy.exc import SQLAlchemyError
from flask import abort

def get_members():
    members = Member.query.all()
    return members

def create_member(**member_data):
    new_member = Member(**member_data)
    try:
        db.session.add(new_member)
        db.session.commit()
        return new_member.to_dict()
    except SQLAlchemyError as e:
        return None

def get_member(id):
    member = Member.query.get_or_404(id)
    if (member is None):
        abort(404)
    return member.to_dict()
