from typing import Tuple

from sqlalchemy import select

from app.db import db
from app.models.users import UsersTable
from app.schemas.users import ResponseGetUser, ResponseFullGetUser, ResponseUserList


def get_full_user_list() -> Tuple[ResponseUserList, int]:
    stmt = select(
        UsersTable.username,
        UsersTable.last_name,
        UsersTable.first_name,
        UsersTable.gender,
        UsersTable.birthday,
        UsersTable.email,
    ).order_by(UsersTable.username)
    result = db.session.execute(stmt)
    users = result.fetchall()
    user_list = [ResponseFullGetUser(
        username=row[0],
        last_name=row[1],
        first_name=row[2],
        gender=row[3],
        birthday=row[4],
        email=row[5],
    ) for row in users]

    return ResponseUserList(users=user_list), 200


def get_username_user_list() -> Tuple[ResponseUserList, int]:
    stmt = select(UsersTable.username).order_by(UsersTable.username)
    result = db.session.execute(stmt)
    users = result.fetchall()
    user_list = [ResponseGetUser(username=row[0]) for row in users]

    return ResponseUserList(users=user_list), 401
