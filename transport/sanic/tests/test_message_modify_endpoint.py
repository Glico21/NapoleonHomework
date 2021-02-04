import pytest

from transport.sanic.endpoints import ModifyMessageEndpoint


@pytest.mark.asyncio
async def test_message_patch_endpoint(request_factory, patched_context, mocker):
    mocker.patch('db.queries.message.patch_message', return_value=None)
    mocker.patch('db.database.DBSession.commit_session', return_value=None)
    mocker.patch('api.base.ResponseDto.__init__', return_value=None)
    mocker.patch('api.base.ResponseDto.dump', return_value=None)

    request = request_factory(method='patch')
    endpoint = ModifyMessageEndpoint(None, patched_context, '', (), False)

    response = await endpoint(request, token={'uid': 1}, message_id=1)
    assert response.status == 200


@pytest.mark.asyncio
async def test_message_delete_endpoint(request_factory, patched_context, mocker):
    mocker.patch('db.queries.message.delete_message', return_value=None)
    mocker.patch('db.database.DBSession.commit_session', return_value=None)
    mocker.patch('api.base.ResponseDto.__init__', return_value=None)
    mocker.patch('api.base.ResponseDto.dump', return_value=None)

    request = request_factory(method='delete')
    endpoint = ModifyMessageEndpoint(None, patched_context, '', (), False)

    response = await endpoint(request, token={'uid': 1}, message_id=1)
    assert response.status == 204
