import os
from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager

from models import db, Member
from api.member_routes import member_routes
from api.auth_routes import auth_routes

from seeds import seed_commands

from config import Config

app = Flask(__name__, static_url_path='', static_folder='../frontend/public')
app.config.from_object(Config)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# app.config.from_object(Config)

# print("SECRET KEY IS: ", app.config["SECRET_KEY"])

# @app.route("/")
# def main():
#     return f'<h1>{app.config["GREETING"]}</h1>'

# if __name__ == "__main__":
#     app.run()
# from flask import Flask
# from config import Config
# app = Flask(__name__)
# app.config.from_object(Config)

# print("SECRET KEY IS: ", app.config["SECRET_KEY"])

# @app.route("/")
# def main():
#     return f'<h1>{app.config["GREETING"]}</h1>'

if __name__ == "__main__":
    app.run(port=5432)







# Setup login manager
login = LoginManager(app)
login.login_view = 'auth.unauthorized'

@login.user_loader
def load_member(id):
    return Member.query.get(int(id))

# Tell flask about our seed commands
app.cli.add_command(seed_commands)
app.register_blueprint(member_routes, url_prefix='/api/members')
# app.register_blueprint(auth_routes, url_prefix='/api/auth')
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
