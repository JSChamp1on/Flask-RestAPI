from flask import Response

from app.csrf import csrf_token
from app.models.users import UsersTable
from app.schemas.users import RequestLoginUser, ResponseLoginUser
from app.services.users.session import set_session


def login_user(body: RequestLoginUser) -> Response:
    response = Response()
    response.content_type = 'application/json'

    existing_user = UsersTable.query.filter_by(
        username=body.username,
        password=body.password,
    ).first()

    if existing_user is None:
        res_body = ResponseLoginUser(
            username=body.username,
            message='\'Username\' or \'password\' already exists',
        )

        response.data = res_body.json()
        response.status_code = 409

        return response

    set_session(current_user=existing_user)

    res_body = ResponseLoginUser(
        username=body.username,
        message='success response msg',
    )

    response.headers['X-CSRFToken'] = csrf_token()
    response.data = res_body.json()
    response.status_code = 200

    return response
