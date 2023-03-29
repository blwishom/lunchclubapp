from flask import Blueprint, jsonify, abort, request
from flask_login import login_required
from services import get_restaurants, create_restaurant, get_restaurant, update_restaurant

restaurant_routes = Blueprint('restaurants', __name__)
# @login_required

@restaurant_routes.route('/', methods=['GET'])
def restaurants():
    restaurants = get_restaurants()
    return jsonify({'restaurants': [restaurant.to_dict() for restaurant in restaurants]})

#create a new restaurant
@restaurant_routes.route('/', methods=['POST'])
@login_required
def create_restaurant_route():
    # add validations
    try:
        new_restaurant = create_restaurant(**request.form)
    except BaseException as e:
        return str(e)
    if (new_restaurant):
        return jsonify(new_restaurant), 201
    else:
        return "Error creating restaurant", 400

#get a specific restaurant
@restaurant_routes.route('/<int:id>', methods=['GET'])
def get_restaurant_route(id):
    restaurant_data = get_restaurant(id)
    return restaurant_data

#edit a specific restaurant
@restaurant_routes.route('/<int:id>', methods=['PATCH'])
@login_required
def update_restaurant_route(id):
    try:
        restaurant_data = update_restaurant(id, **request.form)
        if (restaurant_data):
            return jsonify(restaurant_data), 200
        else:
            return "Error updating restaurant", 400
    except BaseException as e:
        return str(e)