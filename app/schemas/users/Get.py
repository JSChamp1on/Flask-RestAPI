from marshmallow import RAISE, INCLUDE, Schema, fields

from .validate_fields import username, gender, birthday, last_name, first_name


class RequestGetUser(Schema):
    username = fields.String(required=False, validate=username)

    class Meta:
        unknown = RAISE


class ResponseGetUser(Schema):
    username = fields.String(required=True, validate=username)
    gender = fields.String(required=False, validate=gender)
    birthday = fields.Date(required=False, format=birthday)
    last_name = fields.String(required=False, validate=last_name)
    first_name = fields.String(required=False, validate=first_name)

    class Meta:
        unknown = INCLUDE


class ResponseUserList(Schema):
    users = fields.List(fields.Nested(ResponseGetUser), required=True)
