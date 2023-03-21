import os
from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user, login_required
from api.member_routes import member_routes
from api.auth_routes import auth_routes
from api.club_routes import club_routes
from api.restaurant_routes import restaurant_routes

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.login_message_category = "info"

migrate = Migrate()

from models import db, User

from seeds import seed_commands

from config import Config

app = Flask(__name__, static_url_path='', static_folder='../frontend/public')
app.config.from_object(Config)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app = Flask(__name__)
login_manager.init_app(app)
db.init_app(app)
migrate.init_app(app, db)

if __name__ == "__main__":
    app.run(port=5432)

# Setup login manager
login = LoginManager(app)
login.login_view = 'auth.unauthorized'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# Tell flask about our seed commands
app.cli.add_command(seed_commands)

# Register api routes
app.register_blueprint(member_routes, url_prefix='/api/members')
app.register_blueprint(club_routes, url_prefix='/api/clubs')
app.register_blueprint(restaurant_routes, url_prefix='/api/restaurants')
app.register_blueprint(auth_routes, url_prefix='/api/auth')
db.init_app(app)
Migrate(app, db)

# Application Security
CORS(app)

@app.before_request
def https_redirect():
    if os.environ.get('FLASK_ENV') == 'production':
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)

@app.after_request
def inject_csrf_token(response):
    response.set_cookie(
        'csrf_token',
        generate_csrf(),
        secure=True if os.environ.get('FLASK_ENV') == 'production' else False,
        samesite='Strict' if os.environ.get(
            'FLASK_ENV') == 'production' else None,
        httponly=True)
    return response

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    if path == 'favicon.ico':
        return app.send_static_file('favicon.ico')
    return app.send_static_file('index.html')
