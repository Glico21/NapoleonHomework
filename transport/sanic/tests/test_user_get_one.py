import pytest

from transport.sanic.endpoints.user.get_one import OneUserEndpoint


@pytest.mark.asyncio
async def test_one_user_endpoint(request_factory, patched_context, mocker):
    patched_query = mocker.patch('db.queries.user.get_user')
    patched_query.return_value = []

    patched_api = mocker.patch('api.base.ResponseDto.dump')
    patched_api.return_value = None

    patched_schema = mocker.patch('api.base.ResponseDto.__init__')
    patched_schema.return_value = None

    request = request_factory(method='get')
    endpoint = OneUserEndpoint(None, patched_context,  '', ())

    response = await endpoint(request)

    assert response.status == 200
