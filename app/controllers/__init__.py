from flask import Blueprint

from app.controllers.users import users_bp


controllers = Blueprint('controllers', __name__, url_prefix='/api')

users_bp(controllers)
