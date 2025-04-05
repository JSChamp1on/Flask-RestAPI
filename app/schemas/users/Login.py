from marshmallow import RAISE, INCLUDE, Schema, fields

from .validate_fields import username, password


class RequestLoginUser(Schema):
    username = fields.String(required=True, validate=username)
    password = fields.String(required=True, validate=password)

    class Meta:
        unknown = RAISE


class ResponseLoginUser(Schema):
    username = username
    message = fields.String(required=True)

    class Meta:
        unknown = INCLUDE


class ResponseUserStatus(Schema):
    current = fields.String(required=True)
    role = fields.String(required=True)

    class Meta:
        unknown = INCLUDE
