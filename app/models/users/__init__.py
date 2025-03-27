import uuid

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped

from app.db import db


USER_TABLE: str = 'flask_user'
USER_SESSION_TABLE: str = 'flask_user_session'


class UsersTable(db.Model):
    __tablename__: str = USER_TABLE

    id: Mapped[uuid.UUID] = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username: db.String = db.Column(db.String(length=20), nullable=False, unique=True)
    password: db.String = db.Column(db.String(length=16), nullable=False, unique=False)
    gender: db.String = db.Column(db.String(length=6), nullable=False, unique=False)
    birthday: db.String = db.Column(db.String(length=20), nullable=False, unique=False)
    last_name: db.String = db.Column(db.String(length=20), nullable=False, unique=False)
    first_name: db.String = db.Column(db.String(length=20), nullable=False, unique=False)
    email: db.String = db.Column(db.String(length=32), nullable=True, unique=True)


class SessionTable(db.Model):
    __tablename__: str = USER_SESSION_TABLE

    id = db.Column(db.INTEGER(), primary_key=True, autoincrement=True, nullable=False)
    user_id = db.Column(UUID(as_uuid=True), unique=True)
    expiry = db.Column(db.DateTime)
