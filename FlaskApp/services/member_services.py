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


"""
    __tablename__ = 'members'
    __table_args__ = (UniqueConstraint('username', name='uq_members_username'),)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    club_id = db.Column(db.Integer)
    member_info = db.Column( member_type)
    last_login = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    password_digest = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
"""

def update_member(id, **member_data):
    member = Member.query.get_or_404(id)
    if (member is None):
        abort(404)
    member.name = member_data.get('name', member.name)
    member.email = member_data.get('email', member.email)
    member.username = member_data.get('username', member.username)
    member.member_info = member_data.get('member_info', member.member_info)
    member.club_id = member_data.get('club_id', member.club_id)
    try:
        db.session.commit()
        return member.to_dict()
    except SQLAlchemyError as e:
        return None
