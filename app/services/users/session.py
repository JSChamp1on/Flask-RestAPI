from datetime import datetime, timedelta

from flask import session
from sqlalchemy import update, cast, UUID

from app.db import db
from app.models.users import UsersTable, SessionTable


SESSION_NAME: str = 'user_id'
UNAUTHORIZED: str = 'UNAUTHORIZED_401'
USER_NOT_FOUND: str = 'USER_NOT_FOUND_404'
AUTHORIZED: str = 'AUTHORIZED_200'


def session_entry() -> str:
    user_id = session.get(SESSION_NAME)

    entry = db.session.query(SessionTable).filter_by(user_id=user_id).first()

    if entry is None:
        return UNAUTHORIZED

    relevance = entry.expiry > datetime.utcnow()
    if relevance is False:
        return UNAUTHORIZED

    user = UsersTable.query.get(entry.user_id)
    if user is None:
        return USER_NOT_FOUND

    return AUTHORIZED


def set_session(current_user: UsersTable) -> None:
    session[SESSION_NAME] = current_user.id
    session.new = True

    expiry = datetime.utcnow() + timedelta(hours=1)
    stmt = update(SessionTable) \
        .where(SessionTable.user_id == cast(current_user.id, UUID)) \
        .values(
            user_id=current_user.id,
            expiry=expiry,
        )
    result = db.session.execute(stmt)
    if result.rowcount == 0:
        db.session.add(SessionTable(user_id=current_user.id, expiry=expiry))

    db.session.commit()
