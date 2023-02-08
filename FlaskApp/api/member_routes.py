from flask import Blueprint, jsonify
from flask_login import login_required
from models import Member

member_routes = Blueprint('members', __name__)
print('ABOVE USER ROUTE')
# @login_required
@member_routes.route('/', methods=['GET'])
def members():
    members = Member.query.all()
    print('INSIDE USER ROUTE')
    return jsonify({'members': [members.to_dict() for member in members]})

@member_routes.route('/<int:id>')
# @login_required
def member(id):
    member = Member.query.get(id)
    return member.to_dict()
