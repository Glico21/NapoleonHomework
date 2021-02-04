# import pytest
# import bcrypt
#
# from api.request import RequestAuthUserDto
# from db.queries.user import get_user
# from transport.sanic.endpoints.user.auth import AuthUserEndpoint
#
#
# @pytest.mark.asyncio
# async def test_auth_user_endpoint(request_factory, patched_context, mocker, monkeypatch):
#     patched_dto = mocker.patch('api.base.RequestDto.__init__')
#     patched_dto.return_value = None
#
#     patched_query = mocker.patch('db.queries.user.get_user')
#     patched_query.return_value = RequestAuthUserDto
#
#
#
#     monkeypatch.setattr(RequestAuthUserDto, 'login', 0, raising=False)
#     # monkeypatch.setattr(get_user, 'id', 0, raising=False)
#     # monkeypatch.setattr(get_user, 'password', 0, raising=False)
#     monkeypatch.setattr(RequestAuthUserDto, 'password', 0, raising=False)
#
#     patched_hash = mocker.patch(bcrypt, 'checkpw')
#     patched_hash.return_value = None
#
#     request = request_factory(method='post')
#     endpoint = AuthUserEndpoint(None, patched_context, '', (), False)
#
#     response = await endpoint(request)
#     assert response.status == 200
