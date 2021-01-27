from marshmallow import Schema, fields, validate

from api.base import RequestDto


class RequestCreateMessageDtoSchema(Schema):
    message = fields.Str(required=True, allow_none=True, validate=validate.Length(max=280))
    recipient = fields.Str(required=True, allow_none=False)


class RequestCreateMessageDto(RequestDto, RequestCreateMessageDtoSchema):
    __schema__ = RequestCreateMessageDtoSchema
