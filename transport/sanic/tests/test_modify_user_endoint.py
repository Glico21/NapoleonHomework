import pytest

from transport.sanic.endpoints.user.modify import ModifyUserEndpoint


@pytest.mark.asyncio
async def test_patch_user_endpoint(request_factory, patched_context, mocker):
    patched_query = mocker.patch('db.queries.user.patch_user')
    patched_query.return_values = None

    patched_commit = mocker.patch('db.database.DBSession.commit_session')
    patched_commit.return_values = None

    patched_api = mocker.patch('api.base.ResponseDto.dump')
    patched_api.return_value = None

    patched_schema = mocker.patch('api.base.ResponseDto.__init__')
    patched_schema.return_value = None

    request = request_factory(method='patch')
    endpoint = ModifyUserEndpoint(None, patched_context, '', ())

    response = await endpoint(request)

    assert response.status == 200


@pytest.mark.asyncio
async def test_delete_user_endpoint(request_factory, patched_context, mocker):
    patched_query = mocker.patch('db.queries.user.delete_user')
    patched_query.return_values = None

    patched_commit = mocker.patch('db.database.DBSession.commit_session')
    patched_commit.return_values = None
