from flask import Blueprint, jsonify
from flask_login import login_required
from models import Member

member_routes = Blueprint('members', __name__)
# @login_required
@member_routes.route('/', methods=['GET'])
def members():
    members = Member.query.all()
    return jsonify({'members': [member.to_dict() for member in members]})

@member_routes.route('/<int:id>')
# @login_required
def member(id):
    member = Member.query.get(id)
    return member.to_dict()
