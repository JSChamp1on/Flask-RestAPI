from datetime import datetime, timedelta

from flask import session
from sqlalchemy import update, cast
from sqlalchemy.dialects.postgresql import UUID

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

    if entry.user_id is None:
        return USER_NOT_FOUND

    user = UsersTable.query.get(entry.user_id)
    if user is None:
        return USER_NOT_FOUND

    return AUTHORIZED


def update_session() -> None:
    user_id = session.get(SESSION_NAME)

    if user_id is not None:
        session_in(user_id=user_id)


def session_in(user_id: UUID) -> None:
    if user_id is None:
        return None

    session[SESSION_NAME] = user_id
    session.new = True

    _push_user_db(user_id=user_id)


def _push_user_db(user_id: UUID) -> None:
    expiry = datetime.utcnow() + timedelta(hours=1)
    stmt = update(SessionTable) \
        .where(SessionTable.user_id == cast(user_id, UUID)) \
        .values(
        user_id=user_id,
        expiry=expiry,
    )

    result = db.session.execute(stmt)
    if result.rowcount == 0:
        db.session.add(SessionTable(user_id=user_id, expiry=expiry))

    db.session.commit()
