from marshmallow import validate


username = validate.Length(min=3, max=20)
password = validate.Length(min=8, max=12)
gender = validate.OneOf(choices=['male', 'female'])
birthday = '%Y-%m-%d'
last_name = validate.Length(min=2, max=20)
first_name = validate.Length(min=2, max=20)
