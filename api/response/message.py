import datetime

from marshmallow import Schema, pre_load, post_load

from api.base import ResponseDto, Field


class ResponseMessageDtoSchema(Schema):
    id = Field.int()
    sender_id = Field.int()
    recipient_id = Field.int()
    created_at = Field.string()
    updated_at = Field.string()
    message = Field.string()

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


class ResponseMessageDto(ResponseDto, ResponseMessageDtoSchema):
    __schema__ = ResponseMessageDtoSchema
