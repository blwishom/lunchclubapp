from flask import Blueprint, jsonify, session, request
from models import Member, db
from forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required

login_routes = Blueprint('login', __name__)

@login_routes.route('/login', methods=['POST'])
def login():
    """
    Logs a user in
    """
    form = LoginForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        # Add the user to the session, we are logged in!
        member = Member.query.filter(Member.email == form.data['email']).first()
        login_user(member)
        return member.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@login_routes.route('/logout')
def logout():
    """
    Logs a member out
    """
    logout_user()
    return {'message': 'Member logged out'}
