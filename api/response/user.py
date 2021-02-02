import datetime

from marshmallow import Schema, pre_load, post_load

from api.base import ResponseDto, Field


class ResponseUserDtoSchema(Schema):
    id = Field.int()
    login = Field.string()
    created_at = Field.string()
    updated_at = Field.string()
    first_name = Field.string()
    last_name = Field.string()


    @pre_load
    @post_load
    def deserialize_datetime(self, data: dict, **kwargs) -> dict:
        if 'created_at' in data:
            data['created_at'] = self.datetime_to_iso(data['created_at'])
        if 'updated_at' in data:
            data['updated_at'] = self.datetime_to_iso(data['updated_at'])

        return data

    @staticmethod
    def datetime_to_iso(dt):
        if isinstance(dt, datetime.datetime):
            return dt.isoformat()
        return dt


class ResponseUserDto(ResponseDto, ResponseUserDtoSchema):
    __schema__ = ResponseUserDtoSchema
