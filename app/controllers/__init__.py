from flask_smorest import Blueprint

from app.controllers.users import user_blp


user_controller = Blueprint('User', 'user_controller', url_prefix='/api', description='Operations on WSGI')


user_blp(user_controller)
