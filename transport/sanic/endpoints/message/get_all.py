from sanic.request import Request
from sanic.response import BaseHTTPResponse

from transport.sanic.endpoints import BaseEndpoint
from api.response import ResponseMessageDto

from db.database import DBSession
from db.queries import message as message_queries


class GetMessagesEndpoint(BaseEndpoint):

    async def method_get(
            self, request: Request, body: dict, session: DBSession, token: dict, *args, **kwargs
    ) -> BaseHTTPResponse:
        uid = token.get('uid')
        db_message = message_queries.get_messages(session, user_id=uid)
        response_model = ResponseMessageDto(db_message, many=True)

        return await self.make_response_json(status=200, body=response_model.dump())
