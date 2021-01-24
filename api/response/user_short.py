import datetime

from marshmallow import Schema, fields, pre_load, post_load

from api.base import ResponseDto


class ResponseUserShortDtoSchema(Schema):
    login = fields.Str(required=True)
    created_at = fields.Str(required=True)
    updated_at = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)

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


class ResponseUserShortDto(ResponseDto, ResponseUserShortDtoSchema):
    __schema__ = ResponseUserShortDtoSchema