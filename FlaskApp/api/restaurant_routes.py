from flask import Blueprint, jsonify, abort
from flask_login import login_required
from models import Restaurant

restaurant_routes = Blueprint('restaurants', __name__)
# @login_required


@restaurant_routes.route('/', methods=['GET'])
def restaurants():
    restaurants = Restaurant.query.all()
    return jsonify({'restaurants': [restaurant.to_dict() for restaurant in restaurants]})

@restaurant_routes.route('/<int:id>')
# @login_required
def restaurant(id):
    restaurant = Restaurant.query.get_or_404(id)
    if(restaurant is None):
        abort(404)
    return restaurant.to_dict()
