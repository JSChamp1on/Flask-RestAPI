import os

from flask.cli import load_dotenv


load_dotenv()


ENV_DEVl: str = 'development'
ENV_PROD: str = 'production'
NODE_ENV: str = os.getenv('NODE_ENV')

SERV_HOST: str = os.getenv('SERV_HOST')
SERV_PORT: str = os.getenv('SERV_PORT')

APP_SECRET_KEY: str = os.getenv('APP_SECRET_KEY')
WTF_CSRF_SECRET_KEY: str = os.getenv('WTF_CSRF_SECRET_KEY')
SESSION_COOKIE_NAME: str = os.getenv('SESSION_COOKIE_NAME')

DIALECT: str = "postgresql"
DRIVER: str = "psycopg2"
DB_USER: str = os.getenv('DB_USER')
DB_PASS: str = os.getenv('DB_PASS')
DB_HOST: str = os.getenv('DB_HOST')
DB_PORT: str = os.getenv('DB_PORT')
DB_NAME: str = os.getenv('DB_NAME')
