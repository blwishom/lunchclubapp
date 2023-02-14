from models import Club, db
from sqlalchemy.exc import SQLAlchemyError
from flask import abort, jsonify

def get_clubs():
    clubs = Club.query.all()
    return clubs

def create_club(**club_data):
    new_club = Club(**club_data)
    try:
        db.session.add(new_club)
        db.session.commit()
        return new_club.to_dict()
    except SQLAlchemyError as e:
        return None

def get_club(id):
    club = Club.query.get(id)
    if (club is None):
        return jsonify({'error': f"This is not a valid club"})
    return club.to_dict()

def update_club(id, **club_data):
    club = Club.query.get_or_404(id)
    if (club is None):
        abort(404)
    club.name = club_data.get('name', club.name)
    club.location = club_data.get('location', club.location)
    club.join_code = club_data.get('join_code', club.join_code)
    try:
        db.session.commit()
        return club.to_dict()
    except SQLAlchemyError as e:
        return None