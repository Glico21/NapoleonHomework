from marshmallow import Schema, validate

from api.base import RequestDto, Field


class RequestCreateMessageDtoSchema(Schema):
    message = Field.string(allow_none=True, validate=validate.Length(max=280))
    recipient = Field.string()


class RequestCreateMessageDto(RequestDto, RequestCreateMessageDtoSchema):
    __schema__ = RequestCreateMessageDtoSchema
