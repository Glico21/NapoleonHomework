from sanic.request import Request
from sanic.response import BaseHTTPResponse

from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicDialogNotFound
from api.response import ResponseMessageDto

from db.database import DBSession
from db.exceptions import DBMessageNotExistsException
from db.queries import message as message_queries

from helpers.decorators.owner_required import owner_required


class DialogEndpoint(BaseEndpoint):
    @owner_required
    async def method_get(
            self, request: Request, body: dict, session: DBSession, uid: int = None, *args, **kwargs
    ) -> BaseHTTPResponse:

        rid = kwargs.get('rid')

        try:
            db_message = message_queries.get_dialog(session=session, sender_id=uid, recipient_id=rid)
        except DBMessageNotExistsException:
            raise SanicDialogNotFound('Dialog with current user not found')

        response_model = ResponseMessageDto(db_message, many=True)

        return await self.make_response_json(status=200, body=response_model.dump())
