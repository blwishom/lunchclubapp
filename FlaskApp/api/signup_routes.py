from flask import Blueprint, jsonify, session, request
from models import Member, db
from forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required

signup_routes = Blueprint('signup', __name__)

@signup_routes.route('/signup', methods=['POST'])
def sign_up():
    """
    Creates a new member and logs them in
    """
    form = SignUpForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        member = Member(
            username=form.data['username'],
            email=form.data['email'],
            password=form.data['password']
        )
        db.session.add(member)
        db.session.commit()
        login_user(member)
        return member.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401
