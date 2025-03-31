from typing import List, Union

from pydantic import BaseModel, ConfigDict
from marshmallow import RAISE, INCLUDE, Schema, fields


class RequestGetUser(Schema):
    username: str = fields.String(required=False)

    class Meta:
        unknown = RAISE


class ResponseGetUser(Schema):
    username: str = fields.String(required=True)
    gender: str = fields.String(required=False)
    birthday: str = fields.String(required=False)
    last_name: str = fields.String(required=False)
    first_name: str = fields.String(required=False)

    class Meta:
        unknown = INCLUDE


class ResponseUserList(Schema):
    users: list = fields.List(fields.Nested(ResponseGetUser), required=True)
