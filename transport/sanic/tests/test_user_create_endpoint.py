# import pytest
#
# from transport.sanic.endpoints.user.create import CreateUserEndpoint
#
#
# @pytest.mark.asyncio
# async def test_create_user_endpoint(request_factory, patched_context, mocker, monkeypatch):
#     patched_schema = mocker.patch('api.base.RequestDto.__init__')
#     patched_schema.return_value = {
#         'password': None
#     }
#
#     patched_hash = mocker.patch('helpers.passwords.hash.generate_hash')
#     patched_hash.return_value = None
#
#     # monkeypatch.delattr()
#     request = request_factory(method='post')
#     endpoint = CreateUserEndpoint(None, patched_context, '', ())
#
#     response = await endpoint(request)
#
#     assert response.status == 201