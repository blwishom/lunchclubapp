from flask import Blueprint, jsonify
from flask_login import login_required
from models import Club

club_routes = Blueprint('clubs', __name__)
# @login_required


@club_routes.route('/', methods=['GET'])
def clubs():
    clubs = Club.query.all()
    return jsonify({'clubs': [club.to_dict() for club in clubs]})


@club_routes.route('/<int:id>')
# @login_required
def club(id):
    club = Club.query.get(id)
    if(club is None):
        return jsonify({'error': f"This is not a valid club"})
    return club.to_dict()
