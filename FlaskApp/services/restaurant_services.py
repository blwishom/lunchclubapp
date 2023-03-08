from models import Restaurant, db
# from forms import RestaurantForm
from sqlalchemy.exc import SQLAlchemyError
from flask import abort, jsonify
from forms import RestaurantForm, EditRestaurantForm
from wtforms.validators import ValidationError

def get_restaurants():
    restaurants = Restaurant.query.all()
    return restaurants

def create_restaurant(**restaurant_data):
    try:
        form = RestaurantForm(**restaurant_data)
    except ValidationError as e:
        return str(e)
    if form.validate_on_submit():
        new_restaurant = Restaurant(**restaurant_data)
        try:
            db.session.add(new_restaurant)
            db.session.commit()
            return new_restaurant.to_dict()
        except SQLAlchemyError as e:
            return None
    else:
        return { 'errors': str(form.errors)}, 400

def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if (restaurant is None):
        return jsonify({'error': f"This is not a valid restaurant"})
    return restaurant.to_dict()

def update_restaurant(id, **restaurant_data):
    restaurant = Restaurant.query.get_or_404(id)
    if (restaurant is None):
        abort(404)
    try:
        form = EditRestaurantForm(obj=restaurant)
        form.id = restaurant.id
    except ValidationError as e:
        return str(e)

    if form.validate_on_submit():
        form.populate_obj(restaurant)
        try:
            db.session.commit()
            return restaurant.to_dict()
        except SQLAlchemyError as e:
            raise BaseException(str(e))
    else:
        return {'errors': str(form.errors)}, 400