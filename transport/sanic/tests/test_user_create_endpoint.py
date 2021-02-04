import pytest

from transport.sanic.endpoints.user.create import CreateUserEndpoint
from api.request import RequestCreateUserDto


@pytest.mark.asyncio
async def test_create_user_endpoint(request_factory, patched_context, mocker, monkeypatch):
    mocker.patch('api.base.RequestDto.__init__', return_value=None)
    mocker.patch('api.base.ResponseDto.__init__', return_value=None)
    mocker.patch('api.base.ResponseDto.dump', return_value=None)
    mocker.patch('helpers.passwords.hash.generate_hash', return_value=None)
    mocker.patch('db.queries.user.create_user', return_value=None)
    mocker.patch('db.database.DBSession.commit_session', return_value=None)

    monkeypatch.setattr(RequestCreateUserDto, 'password', '0', raising=False)

    request = request_factory(method='post')
    endpoint = CreateUserEndpoint(None, patched_context, '', ())

    response = await endpoint(request)

    assert response.status == 201
