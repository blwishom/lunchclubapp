from flask import Blueprint, jsonify, abort, request
from flask_login import login_required
from models import Member, db
from services import get_members, create_member, get_member, update_member

member_routes = Blueprint('members', __name__)
# @login_required
@member_routes.route('/', methods=['GET'])
def get_members_route():
    members = get_members()
    return jsonify({'members': [member.to_dict() for member in members]})

@member_routes.route('/', methods=['POST'])
def create_member_route():
    # add validations
    new_member = create_member(**request.form)
    if(new_member):
        return jsonify(new_member), 201
    else:
        return "Error creating member", 400

@member_routes.route('/<int:id>', methods=['GET'])
# @login_required
def get_member_route(id):
    member_data = get_member(id)
    return member_data

@member_routes.route('/<int:id>', methods=['PATCH'])
def update_member_route(id):
    member_data = update_member(id, **request.form)
    if(member_data):
        return jsonify(member_data), 200
    else:
        return "Error updating member", 400