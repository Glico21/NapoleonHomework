from sanic.request import Request
from sanic.response import BaseHTTPResponse

from transport.sanic.endpoints import BaseEndpoint
from api.response import ResponseUserShortDto

from db.database import DBSession
from db.queries import user as user_queries
from helpers.decorators import owner_required


class OneUserEndpoint(BaseEndpoint):
    @owner_required
    async def method_get(
            self, request: Request, body: dict, session: DBSession, uid: int = None, *args, **kwargs
    ) -> BaseHTTPResponse:

        db_user = user_queries.get_user(session=session, user_id=uid)

        response_model = ResponseUserShortDto(db_user)

        return await self.make_response_json(status=200, body=response_model.dump())
