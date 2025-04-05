from marshmallow import RAISE, INCLUDE, Schema, fields

from .validate_fields import username, password, gender, birthday, last_name, first_name, email


class RequestRegisterUser(Schema):
    username = username
    password = password
    gender = gender
    birthday = birthday
    last_name = last_name
    first_name = first_name
    email = email

    class Meta:
        unknown = RAISE


class ResponseRegisterUser(Schema):
    username = username
    message = fields.String(required=False)

    class Meta:
        unknown = INCLUDE
