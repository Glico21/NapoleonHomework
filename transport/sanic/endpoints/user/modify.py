from sanic.request import Request
from sanic.response import BaseHTTPResponse

from api.request import RequestPatchUserDto
from api.response import ResponseUserDto
from transport.sanic.endpoints import BaseEndpoint
from transport.sanic.exceptions import SanicUserNotFound, SanicDBException

from db.database import DBSession
from db.exceptions import DBUserNotExistsException, DBDataException, DBIntegrityException
from db.queries import user as user_queries
from helpers.decorators import check_id_rights_access_decorator


class ModifyUserEndpoint(BaseEndpoint):
    @check_id_rights_access_decorator
    async def method_patch(
            self, request: Request, body: dict, session: DBSession, uid: int = None, *args, **kwargs
    ) -> BaseHTTPResponse:

        request_model = RequestPatchUserDto(body)

        try:
            user = user_queries.patch_user(session, request_model, uid)
        except DBUserNotExistsException:
            raise SanicUserNotFound('User not found')

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        response_model = ResponseUserDto(user)

        return await self.make_response_json(status=200, body=response_model.dump())

    @check_id_rights_access_decorator
    async def method_delete(
            self, request: Request, body: dict, session: DBSession, uid: int, *args, **kwargs
    ) -> BaseHTTPResponse:

        try:
            user = user_queries.delete_user(session, uid)
        except DBUserNotExistsException:
            raise SanicUserNotFound('User not found')

        try:
            session.commit_session()
        except (DBDataException, DBIntegrityException) as e:
            raise SanicDBException(str(e))

        return await self.make_response_json(status=204)
