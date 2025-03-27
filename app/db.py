from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.env import DIALECT, DRIVER, DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

uri: str = f"{DIALECT}+{DRIVER}://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

db = SQLAlchemy()
migrate = Migrate()
