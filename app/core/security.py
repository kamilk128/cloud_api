from datetime import datetime, timedelta, timezone
from os import getenv
from argon2.exceptions import VerificationError
from dotenv import load_dotenv
from jose import jwt
from argon2 import PasswordHasher

load_dotenv()

SECRET_KEY = str(getenv("SECRET_KEY"))
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = str(getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_password(plain_password, hashed_password):
    password_hasher = PasswordHasher()
    try:
        return password_hasher.verify(hashed_password, plain_password)
    except VerificationError:
        return False


def get_password_hash(password):
    password_hasher = PasswordHasher()
    return password_hasher.hash(password)
