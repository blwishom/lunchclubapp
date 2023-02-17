from flask import Blueprint, jsonify, session, request
from models import Member, db
from forms import LoginForm
from forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required

auth_routes = Blueprint('auth', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{error}')
    return errorMessages


@auth_routes.route('/')
def authenticate():
    """
    Authenticates a member.
    """
    if current_user.is_authenticated:
        return current_user.to_dict()
    return {'errors': ['Unauthorized']}


@auth_routes.route('/login', methods=['POST'])
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


@auth_routes.route('/logout')
def logout():
    """
    Logs a member out
    """
    logout_user()
    return {'message': 'Member logged out'}


@auth_routes.route('/signup', methods=['POST'])
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


@auth_routes.route('/club-signup', methods=['POST'])
def club_sign_up():
    """
    Creates a new club and logs them in
    """
    form = ClubSignUpForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        club = Club(
            username=form.data['username'],
            email=form.data['email'],
            password=form.data['password']
        )
        db.session.add(club)
        db.session.commit()
        login_user(club)
        return club.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_routes.route('/unauthorized')
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {'errors': ['Unauthorized']}, 401
