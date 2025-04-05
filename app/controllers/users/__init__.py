from flask.views import MethodView
from flask_smorest import Blueprint

from .getUser import get_users
from .loginUser import login_user
from .registerUser import register_user
from .loginUserAuth import login_user_auth
from app.csrf import csrf
from app.schemas.users import (
    RequestGetUser, ResponseUserList,
    RequestLoginUser, ResponseLoginUser,
    RequestRegisterUser, ResponseRegisterUser, ResponseUserStatus,
)


RULE_REGISTER_USER: str = '/register_user'
RULE_LOGIN_USER: str = '/login_user'
RULE_GET_USERS: str = '/get_users'


def user_blp(blp: Blueprint):
    @blp.route(RULE_REGISTER_USER)
    @csrf.exempt
    class RegisterUser(MethodView):
        @blp.arguments(RequestRegisterUser, content_type='application/json')
        @blp.response(201, ResponseRegisterUser, content_type='application/json')
        @blp.alt_response(409, schema=ResponseRegisterUser, content_type='application/json', description='User not found')
        def post(self, body):
            return register_user(body)

    @blp.route(RULE_LOGIN_USER)
    @csrf.exempt
    class LoginUser(MethodView):
        @blp.response(200, ResponseUserStatus, content_type='application/json', description='Authorized')
        @blp.alt_response(401, schema=ResponseUserStatus, content_type='application/json', description='Unauthorized')
        @blp.alt_response(404, schema=ResponseUserStatus, content_type='application/json', description='User not found')
        def get(self):
            return login_user_auth()

        @blp.arguments(RequestLoginUser, content_type='application/json')
        @blp.response(200, ResponseLoginUser, content_type='application/json')
        @blp.alt_response(409, schema=ResponseLoginUser, content_type='application/json', description='User not found')
        def post(self, body):
            return login_user(body)

    @blp.route(RULE_GET_USERS)
    class GetUsers(MethodView):
        @blp.arguments(RequestGetUser, location='query')
        @blp.response(200, ResponseUserList, content_type='application/json')
        @blp.alt_response(401, schema=ResponseUserList, content_type='application/json', description='User not found')
        def get(self, query):
            return get_users(query)
