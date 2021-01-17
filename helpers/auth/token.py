import datetime
import os

import jwt

from dotenv import load_dotenv

from helpers.auth.exceptions import ReadTokenException

load_dotenv()


def create_token(payload: dict):
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(days=1)
    secret = os.getenv('secret', 'INSERT_SECRET_KEY')
    return jwt.encode(payload, secret, algorithm='HS256')


def read_token(token: str) -> dict:
    secret = os.getenv('secret', 'INSERT_SECRET_KEY')

    try:
        return jwt.decode(token, secret, algorithms='HS256')
    except jwt.exceptions.PyJWTError:
        raise ReadTokenException
