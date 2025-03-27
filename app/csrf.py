from flask_wtf.csrf import CSRFProtect, generate_csrf

from app.env import WTF_CSRF_SECRET_KEY

csrf = CSRFProtect()


def csrf_token():
    return generate_csrf(secret_key=WTF_CSRF_SECRET_KEY)
