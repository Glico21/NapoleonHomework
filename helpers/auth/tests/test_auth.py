import datetime

import pytest

from helpers.auth import create_token, read_token, ReadTokenException


@pytest.fixture
def token_data() -> dict:
    return {'id': 1}


# @pytest.fixture()
# def patch_datetime_utcnow(monkeypatch):
#     fake_utcnow = datetime.datetime.utcnow() - datetime.timedelta(days=7)
#
#     class PatchedDatetime:
#         @classmethod
#         def utcnow(cls):
#             return fake_utcnow
#
#     monkeypatch.setattr(datetime, 'datetime', PatchedDatetime)


def test_read_valid_token(token_data):

    request_token = create_token(token_data)
    response_token = read_token(request_token)

    response_token.pop('exp')

    assert response_token == token_data


def test_read_invalid_token():
    token = 'wrong token string'

    with pytest.raises(ReadTokenException):
        read_token(token)


def test_read_expired_token(token_data):

    request_token = create_token(token_data, lifetime=-7)
    with pytest.raises(ReadTokenException):
        read_token(request_token)
