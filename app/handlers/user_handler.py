# -*- coding: utf-8 -*-
# created by lilei at 2020/2/24
from marshmallow import Schema, fields, validate, validates_schema, ValidationError

from app.config import error_codes
from app.config.enums import UserSexEnum
from app.config.exceptions import BusinessException
from app.handlers.base_handler import BaseHandler
from app.schemas.model_schemas import UserModelSchema
from app.schemas.req_schemas import PageListReqSchema
from app.services.user_service import UserService


user_service = UserService()

class UserListHandler(BaseHandler):
    class UserListReqSchema(PageListReqSchema):
        word = fields.Str(required=True, default='')

    def get(self):
        ...


class UserSingleHandler(BaseHandler):
    class UserSingleReqSchema(Schema):
        userId = fields.Int(required=True)

    def get(self):
        print(self.req_form_strict)
        user = user_service.get_by_id(self.req_form_strict['userId'])
        if not user:
            raise BusinessException(error_code=error_codes.USER_NOT_FOUND)
        user_schema = UserModelSchema()
        return self.success(data=user_schema.dump(user))


class UserAddHandler(BaseHandler):
    class UserAddReqSchema(Schema):
        username = fields.Str(required=True, validate=validate.Length(max=128))
        password = fields.Str(required=True, validate=validate.Length(max=256))
        email = fields.Email(required=True)
        sex = fields.Int(required=True, validate=validate.OneOf(UserSexEnum.value_list()))

        @validates_schema
        def validate_email(self, data, **kwargs):
            email = data.get('email', '')
            if not email:
                raise ValidationError('请填写邮箱', 'email')

    def post(self):
        user_model_schema = UserModelSchema()
        user = user_model_schema.load(self.req_form_strict)
        user = user_service.add(user)  # 省略各种校验
        return self.success(data=user)


class UserUpdateHandler(BaseHandler):
    class UserUpdateReqSchema(Schema):
        username = fields.Str(required=True, validate=validate.Length(max=128))
        password = fields.Str(required=True, validate=validate.Length(max=256))
        email = fields.Email(required=True)
        sex = fields.Int(required=True, validate=validate.OneOf(UserSexEnum.value_list()))

    def put(self):
        ...


class UserDelHandler(BaseHandler):
    class UserDelReqSchema(Schema):
        ...

    def delete(self):
        ...