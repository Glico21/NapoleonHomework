from marshmallow import Schema

from api.base import RequestDto, Field


class RequestAuthUserDtoSchema(Schema):
    login = Field.string()
    password = Field.string()


class RequestAuthUserDto(RequestDto, RequestAuthUserDtoSchema):
    __schema__ = RequestAuthUserDtoSchema
