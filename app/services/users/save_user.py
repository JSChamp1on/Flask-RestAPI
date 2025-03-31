from app.db import db
from app.models.users import UsersTable
from app.schemas.users import RequestRegisterUser


def save_user_db(body: RequestRegisterUser) -> None:
    new_user = UsersTable(
        username=body['username'],
        password=body['password'],
        gender=body['gender'],
        birthday=body['birthday'],
        last_name=body['last_name'],
        first_name=body['first_name'],
        email=body['email'],
    )
    db.session.add(new_user)
    db.session.commit()
