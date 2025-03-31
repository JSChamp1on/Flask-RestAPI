from flask.views import MethodView
from flask_smorest import Blueprint

from .get import get_users
from .login import login_user
from .register import register_user
from app.csrf import csrf
from app.schemas.users import (
    RequestGetUser, ResponseUserList,
    RequestLoginUser, ResponseLoginUser,
    RequestRegisterUser, ResponseRegisterUser,
)


def user_blp(blp: Blueprint):
    @blp.route('/register_user')
    @csrf.exempt
    class RegisterUser(MethodView):
        @blp.arguments(RequestRegisterUser, content_type='application/json')
        @blp.response(200, ResponseRegisterUser, content_type='application/json')
        def post(self, body):
            return register_user(body)

    @blp.route('/login_user')
    @csrf.exempt
    class LoginUser(MethodView):
        @blp.arguments(RequestLoginUser, content_type='application/json')
        @blp.response(200, ResponseLoginUser, content_type='application/json')
        def post(self, body):
            return login_user(body)

    @blp.route('/get_users')
    class GetUsers(MethodView):
        @blp.arguments(RequestGetUser, location='query')
        @blp.response(200, ResponseUserList, content_type='application/json')
        def get(self, query):
            return get_users(query)
