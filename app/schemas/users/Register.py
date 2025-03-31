from marshmallow import RAISE, INCLUDE, Schema, fields, validate


class RequestRegisterUser(Schema):
    username: str = fields.String(required=True, validate=validate.Length(min=3, max=20))
    password: str = fields.String(required=True, validate=validate.Length(min=8, max=12))
    gender: str = fields.String(required=True, validate=validate.OneOf(choices=['male', 'female']))
    birthday: str = fields.Date(required=True, format='%Y-%m-%d')
    last_name: str = fields.String(required=True, validate=validate.Length(min=2, max=20))
    first_name: str = fields.String(required=True, validate=validate.Length(min=2, max=20))
    email: str = fields.Email(required=False, missing=None)

    class Meta:
        unknown = RAISE


class ResponseRegisterUser(Schema):
    username: str = fields.String(required=True)
    message: str = fields.String(required=False)

    class Meta:
        unknown = INCLUDE
