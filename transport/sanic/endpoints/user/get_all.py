from sanic.request import Request
from sanic.response import BaseHTTPResponse

from transport.sanic.endpoints import BaseEndpoint
from api.response import ResponseUserDto

from db.database import DBSession
from db.queries import user as user_queries


class AllUserEndpoint(BaseEndpoint):

    async def method_get(
            self, request: Request, body: dict, session: DBSession, *args, **kwargs
    ) -> BaseHTTPResponse:

        db_user = user_queries.get_users(session)
        response_model = ResponseUserDto(db_user, many=True)

        return await self.make_response_json(status=200, body=response_model.dump())
