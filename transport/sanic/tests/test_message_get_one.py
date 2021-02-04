import pytest

from transport.sanic.endpoints.message.get_one import OneMessageEndpoint


@pytest.mark.asyncio
async def test_message_one_endpoint(request_factory, patched_context, mocker):
    patched_query = mocker.patch('db.queries.message.get_message')
    patched_query.return_value = None

    patched_response = mocker.patch('api.base.ResponseDto.__init__')
    patched_response.return_value = None

    patched_response_dump = mocker.patch('api.base.ResponseDto.dump')
    patched_response_dump.return_value = None

    request = request_factory(method='get')
    endpoint = OneMessageEndpoint(None, patched_context, '', (), False)

    response = await endpoint(request, token={'uid': 1}, message_id=1)
    assert response.status == 200
