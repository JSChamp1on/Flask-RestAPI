from typing import Tuple

from flask import Response

from app.schemas.users import RequestGetUser
from app.schemas.users.Get import ResponseUserList
from app.services.users.get_users import get_full_user_list, get_username_user_list
from app.services.users.session import USER_NOT_FOUND, UNAUTHORIZED, AUTHORIZED, session_entry, update_session


def get_users(query: RequestGetUser) -> Tuple[ResponseUserList, int] | Response:
    session_entry_user = session_entry()

    if session_entry_user == UNAUTHORIZED or session_entry_user == USER_NOT_FOUND:
        return get_username_user_list(), 401

    if session_entry_user == AUTHORIZED:
        update_session()
        return get_full_user_list(), 200

    return Response('An unforeseen scenario', status=418)
