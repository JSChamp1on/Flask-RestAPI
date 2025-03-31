from marshmallow import RAISE, INCLUDE, Schema, fields


class RequestLoginUser(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

    class Meta:
        unknown = RAISE


class ResponseLoginUser(Schema):
    username = fields.String(required=True)
    message = fields.String(required=True)

    class Meta:
        unknown = INCLUDE
