from flask import Blueprint, jsonify, request
from flask_login import login_required
from sqlalchemy.exc import SQLAlchemyError
from services import get_clubs, create_club, get_club, update_club

club_routes = Blueprint('clubs', __name__)
# @login_required

@club_routes.route('/', methods=['GET'])
def get_clubs_route():
    clubs = get_clubs()
    return jsonify({'clubs': [club.to_dict() for club in clubs]})


@club_routes.route('/', methods=['POST'])
def create_club_route():
    # add validations
    try:
        new_club = create_club(**request.form)
        return jsonify(new_club), 201
    except SQLAlchemyError as e:
        return jsonify({'status': 'error creating club', 'message': str(e)}), 400


@club_routes.route('/<int:id>', methods=['GET'])
# @login_required
def get_club_route(id):
    club_data = get_club(id)
    return club_data


@club_routes.route('/<int:id>', methods=['PATCH'])
def update_club_route(id):
    try:
        club_data = update_club(id, **request.form)
        return jsonify(club_data), 200
    except SQLAlchemyError as e:
        return jsonify({'status': 'error updating club', 'message': str(e)}), 400