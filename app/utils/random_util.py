# -*- coding: utf-8 -*-
# created by lilei on 2019/11/27
import random
import uuid
import hashlib


def random_str():
    """
    32 位随机字符串
    :return: 字符串
    """
    func = hashlib.md5()
    func.update(str(uuid.uuid4()).encode())
    return func.hexdigest()


def random_code():
    """
    6 位随机验证码
    :return:
    """
    return str(random.randint(0, 999999)).zfill(6)
