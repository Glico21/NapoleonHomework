from marshmallow import Schema, fields, post_load

from api.base import RequestDto


class RequestCreateUserDtoSchema(Schema):
    login = fields.Str(required=True, allow_none=False)
    password = fields.Str(required=True, allow_none=False)
    first_name = fields.Str(required=True, allow_none=False)
    last_name = fields.Str(required=True, allow_none=False)

    # @post_load
    # def hash_password(self, data:dict, **kwargs) -> dict:
    #     data['password'] = generate_hash(data['password'])
    #     return data


class RequestCreateUserDto(RequestDto, RequestCreateUserDtoSchema):
    __schema__ = RequestCreateUserDtoSchema
