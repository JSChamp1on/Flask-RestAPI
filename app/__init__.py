from flask import Flask

from app.models.users import USER_SESSION_TABLE
from app.db import db, uri, migrate
from app.controllers import controllers
from app.csrf import csrf
from app.env import APP_SECRET_KEY, WTF_CSRF_SECRET_KEY, SESSION_COOKIE_NAME


SESSION_TYPE = 'sqlalchemy'


def create_app():
    app = Flask(__name__)

    app.secret_key = APP_SECRET_KEY
    app.config.from_mapping(
        WTF_CSRF_SECRET_KEY=WTF_CSRF_SECRET_KEY,
        SQLALCHEMY_DATABASE_URI=uri,
        SESSION_TYPE=SESSION_TYPE,
        SESSION_SQLALCHEMY_TABLE=USER_SESSION_TABLE,
        SESSION_SQLALCHEMY=db,
        SESSION_COOKIE_NAME=SESSION_COOKIE_NAME,
    )
    app.config.from_object(__name__)
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    app.register_blueprint(controllers)

    return app

