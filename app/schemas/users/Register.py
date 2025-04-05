from marshmallow import RAISE, INCLUDE, Schema, fields

from .validate_fields import username, password, gender, birthday, last_name, first_name


class RequestRegisterUser(Schema):
    username = fields.String(required=True, validate=username)
    password = fields.String(required=True, validate=password)
    gender = fields.String(required=True, validate=gender)
    birthday = fields.Date(required=True, format=birthday)
    last_name = fields.String(required=True, validate=last_name)
    first_name = fields.String(required=True, validate=first_name)
    email = fields.Email(required=False, load_default=None)

    class Meta:
        unknown = RAISE


class ResponseRegisterUser(Schema):
    username = username
    message = fields.String(required=False)

    class Meta:
        unknown = INCLUDE
