import pytest

from transport.sanic.endpoints.user.get_one import OneUserEndpoint


@pytest.mark.asyncio
async def test_one_user_endpoint(request_factory, patched_context, mocker):
    mocker.patch('db.queries.user.get_user', return_value=[])
    mocker.patch('api.base.ResponseDto.dump', return_value=None)
    mocker.patch('api.base.ResponseDto.__init__', return_value=None)

    request = request_factory(method='get')
    endpoint = OneUserEndpoint(None, patched_context,  '', ())

    response = await endpoint(request)

    assert response.status == 200
