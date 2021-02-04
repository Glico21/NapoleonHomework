# import pytest
#
# from api.request import RequestCreateMessageDto
# from db.queries.message import get_user
# from transport.sanic.endpoints import CreateMessageEndpoint
#
#
# @pytest.mark.asyncio
# async def test_message_post_endpoint(request_factory, patched_context, mocker, monkeypatch):
#     mocker.patch('api.base.RequestDto.__init__', return_value=None)
#     mocker.patch('db.queries.message.create_message', return_value=None)
#     mocker.patch('db.queries.message.get_user', return_value=None)
#     mocker.patch('db.database.DBSession.commit_session', return_value=None)
#
#     monkeypatch.setattr(RequestCreateMessageDto, 'recipient', 0, raising=False)
#     monkeypatch.setattr(get_user, 'id', 0, raising=False)
#     request = request_factory(method='post')
#     endpoint = CreateMessageEndpoint(None, patched_context, '', (), False)
#
#     response = await endpoint(request, token={'uid': 1}, message_id=1)
#     assert response.status == 200