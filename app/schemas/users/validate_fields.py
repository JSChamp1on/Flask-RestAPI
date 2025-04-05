from marshmallow import fields, validate


username = fields.String(required=True, validate=validate.Length(min=3, max=20))
password = fields.String(required=True, validate=validate.Length(min=8, max=12))
gender = fields.String(required=True, validate=validate.OneOf(choices=['male', 'female']))
birthday = fields.Date(required=True, format='%Y-%m-%d')
last_name = fields.String(required=True, validate=validate.Length(min=2, max=20))
first_name = fields.String(required=True, validate=validate.Length(min=2, max=20))
email = fields.Email(required=False, load_default=None)
