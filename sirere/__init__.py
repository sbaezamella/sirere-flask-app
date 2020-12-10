import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import config

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


def create_app(config_name=None):
    app = Flask(__name__, static_folder='./static')

    if config_name is None:
        config_name = os.getenv('SIRERE_CONFIG', 'development')

    app.config.from_object(config.get(config_name))

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from sirere.models import Usuario

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return Usuario.query.get(int(user_id))

    # blueprint for auth routes in our app
    from sirere.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from sirere.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
