from sanic.request import Request
from sanic.response import BaseHTTPResponse

from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDBException, SanicMessageNotFound
from api.request import RequestPatchMessageDto
from api.response import ResponseMessageDto

from db.database import DBSession
from db.exceptions import DBDataException, DBIntegrityException, DBMessageNotExistsException
from db.queries import message as message_queries


class ModifyMessageEndpoint(BaseEndpoint):
    async def method_patch(
            self, request: Request, body: dict, session: DBSession, message_id: int, token: dict, *args, **kwargs
    ) -> BaseHTTPResponse:

        request_model = RequestPatchMessageDto(body)

        uid = token.get('uid')

        try:
            message = message_queries.patch_message(session, request_model, user_id=uid, message_id=message_id)
        except DBMessageNotExistsException:
            raise SanicMessageNotFound('Message not found')

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseMessageDto(message)

        return await self.make_response_json(status=200, body=response_model.dump())

    async def method_delete(
            self, request: Request, body: dict, session: DBSession, message_id: int, token: dict, *args, **kwargs
    ) -> BaseHTTPResponse:

        uid = token.get('uid')

        try:
            message = message_queries.delete_message(session, message_id=message_id, user_id=uid)
        except DBMessageNotExistsException:
            raise SanicMessageNotFound('Message not found')

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        return await self.make_response_json(status=204)
