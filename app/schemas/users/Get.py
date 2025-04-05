from marshmallow import RAISE, INCLUDE, Schema, fields

from .validate_fields import username, gender, birthday, last_name, first_name


class RequestGetUser(Schema):
    username = username

    class Meta:
        unknown = RAISE


class ResponseGetUser(Schema):
    username = username
    gender = gender
    birthday = birthday
    last_name = last_name
    first_name = first_name

    class Meta:
        unknown = INCLUDE


class ResponseUserList(Schema):
    users = fields.List(fields.Nested(ResponseGetUser), required=True)
