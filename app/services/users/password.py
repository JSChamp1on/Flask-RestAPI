import os
from base64 import urlsafe_b64encode, urlsafe_b64decode

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

from app.models.users import PASSWORD_LENGTH


_B_GEN: int = round(PASSWORD_LENGTH / 3)


def hash_pwd(password: str) -> str:
    b_pwd = bytes(password, 'utf-8')

    salt = os.urandom(_B_GEN)

    kdf = _kdf(salt)

    key = kdf.derive(b_pwd)

    base64key = urlsafe_b64encode(salt + key)

    return base64key.decode()


def verify_pwd(provided_password: str, stored_password: str) -> bool:
    decoded = urlsafe_b64decode(stored_password)

    salt = decoded[:_B_GEN]
    b_stored_pwd = decoded[_B_GEN:]

    kdf = _kdf(salt)

    b_provided_pwd = kdf.derive(provided_password.encode())
    return b_provided_pwd == b_stored_pwd


def _kdf(salt):
    return PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=_B_GEN,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
