from flask import Flask
from flask_smorest import Api

from app.config import SERV_HOST, SERV_PORT


def swagger_init(app: Flask) -> Api:
    app.config.update(
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
    api = Api()
    api.init_app(app)
    api.spec.options['servers'] = [
        {
            "url": f"http://{SERV_HOST}:{SERV_PORT}",
            "description": "Local development server"
        },
    ]

    return api
