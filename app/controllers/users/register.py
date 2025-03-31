from typing import Tuple

from app.models.users import UsersTable
from app.schemas.users import RequestRegisterUser, ResponseRegisterUser, responseRegisterUser
from app.services.users.save_user import save_user_db


def register_user(body: RequestRegisterUser) -> Tuple[ResponseRegisterUser, int]:
    existing_username = UsersTable.query.filter_by(username=body['username']).first()
    existing_email = UsersTable.query.filter_by(email=body['email']).first()
    if existing_username or existing_email and existing_email.email is not None:
        return responseRegisterUser.dump({
            "username": body['username'],
            "email": body['email'],
            "message": '\'Username\' or \'email\' already exists',
        }), 409

    save_user_db(body=body)

    return responseRegisterUser.dump({
        "username": body['username'],
        "message": 'success created',
    }), 201
