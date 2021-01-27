from sanic.request import Request
from sanic.response import BaseHTTPResponse

from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicPasswordHashException, SanicUserConflictException
from api.request import RequestCreateUserDto
from api.response import ResponseUserDto

from db.queries import user as user_queries
from db.exceptions import DBDataException, DBIntegrityException, DBUserExistsException
from helpers.passwords import generate_hash
from helpers.passwords import GeneratePasswordHashException


class CreateUserEndpoint(BaseEndpoint):

    async def method_post(self, request: Request, body: dict, session, *args, **kwargs) -> BaseHTTPResponse:

        request_model = RequestCreateUserDto(body)

        try:
            hashed_password = generate_hash(request_model.password)
        except GeneratePasswordHashException:
            raise SanicPasswordHashException('Wrong password')

        try:
            db_user = user_queries.create_user(session, request_model, hashed_password)
        except DBUserExistsException:
            raise SanicUserConflictException('Login is busy')

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            return await self.make_response_json(status=500, message=str(e))
        response_model = ResponseUserDto(db_user)

        return await self.make_response_json(body=response_model.dump(), status=201)
