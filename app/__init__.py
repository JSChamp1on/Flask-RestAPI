import yaml
from flask import Flask
from flask_smorest import Api

from app.models.users import USER_SESSION_TABLE
from app.db import db, uri, migrate
from app.controllers import user_controller
from app.csrf import csrf
from app.env import APP_SECRET_KEY, WTF_CSRF_SECRET_KEY, SESSION_COOKIE_NAME, SERV_HOST, SERV_PORT


SESSION_TYPE = 'sqlalchemy'


api = Api()


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
        API_TITLE='Library API',
        API_VERSION='v0.0.1',
        OPENAPI_VERSION='3.1.0',
        OPENAPI_DESCRIPTION='A simple library API',
        OPENAPI_URL_PREFIX='/',
        OPENAPI_SWAGGER_UI_PATH='/swagger-ui',
        OPENAPI_SWAGGER_UI_URL='https://cdn.jsdelivr.net/npm/swagger-ui-dist/',
        API_SPEC_OPTIONS={
            "x-speakeasy-retries": {
                'strategy': 'backoff',
                'backoff': {
                    'initialInterval': 500,
                    'maxInterval': 60000,
                    'maxElapsedTime': 3600000,
                    'exponent': 1.5,
                },
                'statusCodes': ['5XX'],
                'retryConnectionErrors': True,
            }
        },
    )
    app.config.from_object(__name__)
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    api.init_app(app)
    api.register_blueprint(user_controller)
    api.spec.options['servers'] = [
        {
            "url": f"http://{SERV_HOST}:{SERV_PORT}",
            "description": "Local development server"
        }
    ]

    @app.route("/openapi.yaml")
    def openapi_yaml():
        spec = api.spec.to_dict()
        return app.response_class(
            yaml.dump(spec, default_flow_style=False),
            mimetype="application/x-yaml"
        )

    return app

