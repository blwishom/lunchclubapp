from flask import Blueprint, jsonify
from flask_login import login_required
from models import Member

user_routes = Blueprint('users', __name__)

@user_routes.route('/', methods=['GET'])
# @login_required
def users():
    users = User.query.all()
    return jsonify({'users': [user.to_dict() for user in users]})

@user_routes.route('/<int:id>')
@login_required
def user(id):
    user = User.query.get(id)
    return user.to_dict()
