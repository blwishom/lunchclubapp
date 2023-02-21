from flask import Blueprint, jsonify, request
from flask_login import login_required
from models import Club
from services import get_clubs, create_club, get_club, update_club

club_routes = Blueprint('clubs', __name__)
# @login_required

#get all clubs
@club_routes.route('/', methods=['GET'])
def get_clubs_route():
    clubs = get_clubs()
    return jsonify({'clubs': [club.to_dict() for club in clubs]})


#create a new club
@club_routes.route('/new-club', methods=['POST'])
def create_club_route():
    # add validations
    new_club = create_club(**request.form)
    if (new_club):
        return jsonify(new_club), 201
    else:
        return "Error creating club", 400

#get a specific club
@club_routes.route('/<int:id>', methods=['GET'])
# @login_required
def get_club_route(id):
    club_data = get_club(id)
    return club_data

#edit a specific club
@club_routes.route('/<int:id>', methods=['PATCH'])
def update_club_route(id):
    club_data = update_club(id, **request.form)
    if (club_data):
        return jsonify(club_data), 200
    else:
        return "Error updating club", 400
