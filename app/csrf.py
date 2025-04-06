from flask_wtf.csrf import CSRFProtect, generate_csrf

from app.config import WTF_CSRF_SECRET_KEY


csrf = CSRFProtect()


def csrf_token():
    return generate_csrf(secret_key=WTF_CSRF_SECRET_KEY)
