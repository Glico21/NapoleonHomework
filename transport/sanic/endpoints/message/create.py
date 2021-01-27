from sanic.request import Request
from sanic.response import BaseHTTPResponse

from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicUserNotFound
from api.request import RequestCreateMessageDto
from api.response import ResponseMessageDto

from db.database import DBSession
from db.queries import message as message_queries
from db.exceptions import DBUserNotExistsException, DBDataException, DBIntegrityException


class CreateMessageEndpoint(BaseEndpoint):

    async def method_post(
            self, request: Request, body: dict, session: DBSession, token: dict, *args, **kwargs
    ) -> BaseHTTPResponse:

        request_model = RequestCreateMessageDto(body)

        try:
            recipient = message_queries.get_user(session=session, login=request_model.recipient)
        except DBUserNotExistsException:
            raise SanicUserNotFound('Recipient not found')

        uid = token.get('uid')

        try:
            sender = message_queries.get_user(session=session, user_id=uid)
        except DBUserNotExistsException:
            raise SanicUserNotFound('Sender not found')

        converse_id = {
            'sender_id': sender.id,
            'recipient_id': recipient.id
        }

        db_message = message_queries.create_message(session, request_model, converse_id)

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            return await self.make_response_json(status=500, message=str(e))

        response_model = ResponseMessageDto(db_message)

        return await self.make_response_json(body=response_model.dump(), status=201)
