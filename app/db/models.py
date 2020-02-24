# -*- coding: utf-8 -*-
# created by lilei on 2019/11/7
import datetime
import enum
import re
from sqlalchemy.ext.declarative import declared_attr

from app.config.enums import BaseEnum, UserSexEnum
from ..db import db


class IntEnum(db.TypeDecorator):
    """
    int enum
    """

    impl = db.SmallInteger

    def __init__(self, enum_type=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._enum_type = enum_type

    def process_bind_param(self, value, dialect):
        if isinstance(value, int):
            return value

        if isinstance(value, BaseEnum):
            return value.value

        return value

    def process_result_value(self, value, dialect):
        return self._enum_type(value)

    def process_literal_param(self, value, dialect):
        pass

    def python_type(self):
        return type(enum.Enum)


class BaseModel(db.Model):
    __abstract__ = True

    @declared_attr
    def __tablename__(self):
        model_name = re.sub('(?<!^)(?=[A-Z])', '_', self.__name__).lower()
        if model_name.endswith('_model'):
            return model_name.replace('_model', '')
        return model_name

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True, comment="自增id")
    create_time = db.Column(db.DateTime, index=True, nullable=False, server_default=db.text('NOW()'), comment="创建时间")
    update_time = db.Column(db.DateTime, index=True, nullable=False, server_default=db.text('NOW()'),
                            onupdate=datetime.datetime.now, comment="更新时间")
    delete_time = db.Column(db.DateTime, index=True, nullable=True, comment="删除时间")


class User(BaseModel):

    # __tablename__ = 'user'

    # __searchable__ = ['username', 'email']

    username = db.Column(db.String(128), nullable=False, unique=True, comment='用户名')
    password = db.Column(db.String(256), nullable=False, comment='密码')
    email = db.Column(db.String(32), nullable=False, comment='邮箱')
    sex = db.Column(IntEnum(UserSexEnum), nullable=False, comment='性别')

    def __str__(self):
        return self.username
