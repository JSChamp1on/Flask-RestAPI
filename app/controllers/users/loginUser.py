import json

from flask import Response

from app.csrf import csrf_token
from app.models.users import UsersTable
from app.schemas.users import RequestLoginUser, responseLoginUser
from app.services.users.password import verify_pwd
from app.services.users.session import session_in


def login_user(body: RequestLoginUser) -> Response:
    response = Response()
    response.content_type = 'application/json'

    existing_user = UsersTable.query.filter_by(
        username=body['username'],
    ).first()

    if existing_user is None:
        res_body = responseLoginUser.dump({
            "username": body['username'],
            "message": 'Username already exists',
        })

        response.data = json.dumps(res_body).encode('utf-8')
        response.status_code = 409

        return response

    valid_pwd = verify_pwd(
        provided_password=body['password'],
        stored_password=existing_user.password,
    )

    if valid_pwd is False:
        res_body = responseLoginUser.dump({
            "username": body['username'],
            "message": 'Password already exists',
        })

        response.data = json.dumps(res_body).encode('utf-8')
        response.status_code = 409

        return response

    session_in(user_id=existing_user.id)

    res_body = responseLoginUser.dump({
        "username": body['username'],
        "message": 'Success response',
    })

    response.headers['X-CSRFToken'] = csrf_token()
    response.data = json.dumps(res_body).encode('utf-8')
    response.status_code = 200

    return response
