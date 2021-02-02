from marshmallow import Schema, fields

from api.base import RequestDto, Field


class RequestCreateUserDtoSchema(Schema):
    login = Field.string()
    password = Field.string()
    first_name = Field.string()
    last_name = Field.string()


class RequestCreateUserDto(RequestDto, RequestCreateUserDtoSchema):
    __schema__ = RequestCreateUserDtoSchema
