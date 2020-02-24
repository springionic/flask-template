# -*- coding: utf-8 -*-
# created by lilei on 2019/11/7


PROJECT_NAME = 'server-template'


def __build_redis_key(key):
    """
    redis key 统一添加项目名作为前缀
    """
    return '%s:%s' % (PROJECT_NAME, key)


# 请求头
REQ_HEADER_KEY_UID = 'X-YL-Uid'
REQ_HEADER_KEY_TOKEN = 'X-YL-Token'
REQ_HEADER_KEY_USER = 'X-YL-User'
