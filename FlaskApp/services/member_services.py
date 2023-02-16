from models import Member, db
from sqlalchemy.exc import SQLAlchemyError
from flask import abort

def get_members():
    members = Member.query.all()
    return members

def create_member(**member_data):
    new_member = Member(**member_data)
    try:
        new_member.validate()
    except ValueError as e:
        raise e

    try:
        db.session.add(new_member)
        db.session.commit()
        return new_member.to_dict()
    except SQLAlchemyError as e:
        raise e

def get_member(id):
    member = Member.query.get_or_404(id)
    if (member is None):
        abort(404)
    return member.to_dict()

def update_member(id, **member_data):
    member = Member.query.get_or_404(id)
    if (member is None):
        abort(404)
    member.name = member_data.get('name', member.name)
    member.email = member_data.get('email', member.email)
    member.username = member_data.get('username', member.username)
    member.member_info = member_data.get('member_info', member.member_info)
    member.club_id = member_data.get('club_id', member.club_id)
    tentative_member = Member(name=member.name, email=member.email, username=member.username, member_info=member.member_info, club_id=member.club_id)

    try:
        tentative_member.validate()
    except ValueError as e:
        raise e

    try:
        db.session.commit()
        return member.to_dict()
    except SQLAlchemyError as e:
        raise e
