# -*- coding: utf-8 -*-
# created by lilei on 2019/11/7
from enum import Enum, unique


@unique
class BaseEnum(Enum):
    @classmethod
    def has_value(cls, value):
        """
        判断枚举类型是否包含枚举值 value
        :param value: 枚举值
        :return: True or False
        """
        return any(value == item.value for item in cls)

    @classmethod
    def value_list(cls):
        """
        值列表
        :return: tuple
        """
        return [item.value for item in cls]

    @classmethod
    def parse_value(cls, value):
        """
        值转换为枚举
        :param value: 值
        :return: enum
        """
        for item in cls:
            if value == item.value:
                return item
        return None


class UserSexEnum(BaseEnum):
    """
    用户性别枚举
    """
    UNKNOWN = 0  # 未知
    MALE = 1  # 男
    FEMALE = 2  # 女
