from app.db import db
from app.models.users import UsersTable
from app.schemas.users import RequestRegisterUser
from app.services.users.password import hash_pwd


def insert_user_db(body: RequestRegisterUser) -> None:
    hash_password = hash_pwd(password=body['password'])

    new_user = UsersTable(
        username=body['username'],
        password=hash_password,
        gender=body['gender'],
        birthday=body['birthday'],
        last_name=body['last_name'],
        first_name=body['first_name'],
        email=body['email'],
    )
    db.session.add(new_user)
    db.session.commit()
