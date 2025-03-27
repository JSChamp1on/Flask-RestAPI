from flask import Blueprint
from flask_pydantic import validate

from .get import get_users
from .login import login_user
from .register import register_user
from app.csrf import csrf
from app.schemas.users import (
    RequestGetUser,
    RequestLoginUser,
    RequestRegisterUser,
)


def users_bp(blueprint: Blueprint):
    @blueprint.route('/get_users', methods=['GET'])
    @validate()
    def handle_get_user(query: RequestGetUser):
        return get_users(query)

    @blueprint.route('/login_user', methods=['POST'])
    @csrf.exempt
    @validate()
    def handle_login(body: RequestLoginUser):
        return login_user(body)

    @blueprint.route('/register_user', methods=['POST'])
    @csrf.exempt
    @validate()
    def handle_register_user(body: RequestRegisterUser):
        return register_user(body)
