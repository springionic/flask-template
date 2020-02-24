# -*- coding: utf-8 -*-
# created by lilei on 2019/11/8


# 错误码规则：AABBCC
# A：服务编码（2 位）
# B：服务内模块编码（2 位）
# C：模块内编码（2 位）

# 公共错误码，应与具体业务和模块无关
SERVER_INTERVAL_ERROR = (100000, '服务器内部错误')
SERVER_PATH_NOT_FOUND = (100001, '请求路径不存在')
SERVER_PARAM_INVALID = (100002, '请求参数不合法或缺失')
SERVER_METHOD_NOT_ALLOWED = (100003, '请求方法不正确')
SERVER_BAD_REQUEST = (100004, '请求语法不正确')
SERVER_METHOD_OR_PATH_ERROR = (100005, '路径或方法有误')
SERVER_HEADERS_REQUIRED = (100006, '缺少必要请求头或者不正确')
SERVER_REQUEST_EXPIRED = (100007, '请求已过期')
SERVER_LOGIN_REQUIRED = (100008, '请登录')
SERVER_NO_PERMISSION = (100009, '无权限')

# 服务编码 11

# 模块编码00
USER_REPEAT = (110000, '用户名重复')
USER_NOT_FOUND = (110001, '用户不存在')
