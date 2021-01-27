from sanic.request import Request
from sanic.response import BaseHTTPResponse

from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicMessageNotFound
from api.response import ResponseMessageDto

from db.database import DBSession
from db.queries import message as message_queries
from db.exceptions import DBMessageNotExistsException


class OneMessageEndpoint(BaseEndpoint):
    async def method_get(
            self, request: Request, body: dict, session: DBSession, token: dict, message_id: int, *args, **kwargs
    ) -> BaseHTTPResponse:

        uid = token.get('uid')

        try:
            db_message = message_queries.get_message(session=session, message_id=message_id, user_id=uid)
        except DBMessageNotExistsException:
            raise SanicMessageNotFound('Message not found')

        response_model = ResponseMessageDto(db_message)

        return await self.make_response_json(status=200, body=response_model.dump())
