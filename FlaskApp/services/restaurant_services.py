from models import Restaurant, db
# from forms import ClubForm
from sqlalchemy.exc import SQLAlchemyError
from flask import abort, jsonify

def get_restaurant():
    restaurant = Restaurant.query.all()
    return restaurant

def create_restaurant(**restaurant_data):
    form = RestraurantForm(request.form)
    if form.validate_on_submit():
        new_restaurant = Restraurant(**restaurant_data)
        db.session.add(new_restaurant)
        db.session.commit()
        return restaurant.to_dict()
    else:
        return { 'errors': validation_errors_to_error_messages(form.errors)}, 400
    try:
        db.session.add(new_restaurant)
        db.session.commit()
        return new_restaurant.to_dict()
    except SQLAlchemyError as e:
        return None

def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if (restaurant is None):
        return jsonify({'error': f"This is not a valid club"})
    return restaurant.to_dict()

def update_restaurant(id, **restaurant_data):
    restaurant = Club.query.get_or_404(id)
    if (restaurant is None):
        abort(404)
    restaurant.name = restaurant_data.get('name', restaurant.name)
    restaurant.address = restaurant_data.get('address', restaurant.address)
    try:
        db.session.commit()
        return restaurant.to_dict()
    except SQLAlchemyError as e:
        return None
