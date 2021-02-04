import pytest

from transport.sanic.endpoints.message.get_all import GetMessagesEndpoint


@pytest.mark.asyncio
async def test_all_messages_endpoint(request_factory, patched_context, mocker):
    mocker.patch('db.queries.message.get_messages', return_value=[])
    mocker.patch('transport.sanic.base.SanicEndpoint.import_body_auth', return_value={'uid': 0})

    request = request_factory(method='get')
    endpoint = GetMessagesEndpoint(None, patched_context, '', (), True)

    response = await endpoint(request)
    assert response.status == 200
