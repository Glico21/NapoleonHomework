import pytest

from transport.sanic.endpoints.user.modify import ModifyUserEndpoint


@pytest.mark.asyncio
async def test_patch_user_endpoint(request_factory, patched_context, mocker):
    mocker.patch('db.queries.user.patch_user', return_value=None)
    mocker.patch('db.database.DBSession.commit_session', return_value=None)
    mocker.patch('api.base.ResponseDto.dump', return_value=None)
    mocker.patch('api.base.ResponseDto.__init__', return_value=None)

    request = request_factory(method='patch')
    endpoint = ModifyUserEndpoint(None, patched_context, '', ())

    response = await endpoint(request)

    assert response.status == 200


@pytest.mark.asyncio
async def test_delete_user_endpoint(request_factory, patched_context, mocker):
    mocker.patch('db.queries.user.delete_user', return_value=None)
    mocker.patch('helpers.decorators.owner_required', return_value=None)
    mocker.patch('db.database.DBSession.commit_session', return_value=None)

    request = request_factory(method='delete')
    endpoint = ModifyUserEndpoint(None, patched_context, '', (), False)

    response = await endpoint(request, token={'uid': 1}, message_id=1, uid=1)

    assert response.status == 204
