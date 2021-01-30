import pytest

from transport.sanic.endpoints.user.get_all import AllUserEndpoint


@pytest.mark.asyncio
async def test_all_user_endpoint(request_factory, patched_context, mocker):
    patched_query = mocker.patch('db.queries.user.get_users')
    patched_query.return_value = []

    request = request_factory(method='get')
    endpoint = AllUserEndpoint(None, patched_context, '', ())

    response = await endpoint(request)

    assert response.status == 200
