import uuid

from sqlalchemy.orm import Mapped
from sqlalchemy.dialects.postgresql import UUID

from app.db import db


USER_TABLE: str = 'flask_user'
USER_SESSION_TABLE: str = 'flask_user_session'

PASSWORD_LENGTH: int = 64


class UsersTable(db.Model):
    __tablename__: str = USER_TABLE

    id: Mapped[uuid.UUID] = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username: db.String = db.Column(db.String(length=20), nullable=False, unique=True)
    password: db.String = db.Column(db.String(length=PASSWORD_LENGTH), nullable=False, unique=False)
    gender: db.String = db.Column(db.String(length=6), nullable=False, unique=False)
    birthday: db.DateTime = db.Column(db.DateTime, nullable=False, unique=False)
    last_name: db.String = db.Column(db.String(length=20), nullable=True, unique=False)
    first_name: db.String = db.Column(db.String(length=20), nullable=True, unique=False)
    email: db.String = db.Column(db.String(length=32), nullable=True, unique=True)


class SessionTable(db.Model):
    __tablename__: str = USER_SESSION_TABLE

    id: db.INTEGER = db.Column(db.INTEGER(), primary_key=True, autoincrement=True, nullable=False)
    user_id: Mapped[uuid.UUID] = db.Column(UUID(as_uuid=True), nullable=False, unique=True)
    expiry: db.DateTime = db.Column(db.DateTime, nullable=False, unique=False)
