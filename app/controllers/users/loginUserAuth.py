from typing import Tuple

from app.schemas.users import responseUserStatus, ResponseUserStatus
from app.services.users.session import AUTHORIZED, UNAUTHORIZED, USER_NOT_FOUND, session_entry, update_session


def login_user_auth() -> Tuple[ResponseUserStatus, int]:
    entry = session_entry()

    res_code = 200

    if entry is AUTHORIZED:
        update_session()

    if entry is UNAUTHORIZED:
        res_code = 401

    if entry is USER_NOT_FOUND:
        res_code = 404

    return responseUserStatus.dump({
        "current": entry,
        "role": "user",
    }), res_code
