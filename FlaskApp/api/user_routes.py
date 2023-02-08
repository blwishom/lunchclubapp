from flask import Blueprint, jsonify
from flask_login import login_required
from models import Member

user_routes = Blueprint('members', __name__)

@user_routes.route('/', methods=['GET'])
# @login_required
def members():
    members = Member.query.all()
    return jsonify({'members': [member.to_dict() for member in members]})

@user_routes.route('/<int:id>')
@login_required
def member(id):
    member = Member.query.get(id)
    return member.to_dict()
