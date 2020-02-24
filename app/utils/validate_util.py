# -*- coding: utf-8 -*-
# created by lilei on 2019/11/10
import re
from typing.re import Pattern


def _is_valid(pattern: Pattern, value):
    return True if re.match(pattern, value) else False


def phone_is_valid(phone):
    """
    手机号码格式校验
    """
    pattern = r'^1[3456789]\d{9}$'
    return _is_valid(pattern, phone)


def username_is_valid(username):
    """
    用户名格式验证
    1. 字母、数字和 _ 符号组合，不允许纯数字或 _ 符号
    2. 4-20 位
    """
    pattern = r'^(?![0-9]+$)(?!_+)[0-9A-Za-z_]{4,20}$'
    return _is_valid(pattern, username)


def email_is_valid(email):
    """
    邮箱格式校验
    """
    pattern = r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
    return _is_valid(pattern, email)


def password_is_valid(password):
    """
    密码格式校验
    目前仅校验长度，6-32 位任意字符即可
    """
    return 6 <= len(password) <= 32


def current_page_is_valid(current_page):
    """
    当前页码是否合法，页码从 1 开始
    """
    return current_page > 0


def page_size_is_valid(page_size):
    """
    每页条目数是否合法，至少 1 条
    """
    return page_size > 0
