from flask import Flask

from app.models.users import USER_SESSION_TABLE
from app.db import db, uri, migrate
from app.controllers import user_controller
from app.csrf import csrf
from app.config import (
    APP_SECRET_KEY,
    WTF_CSRF_SECRET_KEY,
    SESSION_TYPE,
    SESSION_COOKIE_NAME,
    NODE_ENV,
    ENV_DEVl,
    ENV_PROD,
)
from app.specification import swagger_init


def create_app():
    app = Flask(__name__)

    app.secret_key = APP_SECRET_KEY
    app.config.from_object(__name__)
    app.config.from_mapping(
        WTF_CSRF_SECRET_KEY=WTF_CSRF_SECRET_KEY,
        SQLALCHEMY_DATABASE_URI=uri,
        SESSION_TYPE=SESSION_TYPE,
        SESSION_SQLALCHEMY_TABLE=USER_SESSION_TABLE,
        SESSION_SQLALCHEMY=db,
        SESSION_COOKIE_NAME=SESSION_COOKIE_NAME,
    )
    if NODE_ENV == ENV_DEVl:
        api = swagger_init(app)
        api.register_blueprint(user_controller)
    elif NODE_ENV == ENV_PROD:
        app.register_blueprint(user_controller)
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    return app
