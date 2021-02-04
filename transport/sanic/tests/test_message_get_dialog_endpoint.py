# import pytest
#
# from transport.sanic.endpoints import DialogEndpoint
#
#
# @pytest.mark.asyncio
# async def test_message_dialog_endpoint(request_factory, patched_context, mocker, monkeypatch):
#     mocker.patch('helpers.decorators.owner_required.owner_required', return_value=None)
#     request = request_factory(method='get')
#     endpoint = DialogEndpoint(None, patched_context, '', (), False)
#     response = await endpoint(request, token={'uid': 1}, message_id=1)
#     assert response.status == 200