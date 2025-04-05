from flask_smorest import Blueprint

from app.controllers.users import user_blp


PREFIX_METHODS: str = '/api'


user_controller = Blueprint('User', 'user_controller', url_prefix=PREFIX_METHODS, description='Operations on WSGI')


user_blp(user_controller)
