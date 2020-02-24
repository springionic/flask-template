# -*- coding: utf-8 -*-
# created by lilei on 2019/11/10
from flask.debughelpers import FormDataRoutingRedirect
from werkzeug.exceptions import MethodNotAllowed, BadRequest, NotFound

from app.components import logger
from app.config import error_codes
from app.config.exceptions import MyBaseException
from app.handlers.base_handler import BaseHandler

HTTP_EXCEPTION_ERROR_CODE_MAP = {
    MethodNotAllowed: error_codes.SERVER_METHOD_NOT_ALLOWED,
    BadRequest: error_codes.SERVER_BAD_REQUEST,
    NotFound: error_codes.SERVER_PATH_NOT_FOUND,
    FormDataRoutingRedirect: error_codes.SERVER_PATH_NOT_FOUND
}

error_logger = logger.get_logger('error_logger')


def handler_error(e):
    """
    全局异常处理
    """
    if isinstance(e, MyBaseException):
        error_code = (getattr(e, 'code'), getattr(e, 'msg'))
        data = getattr(e, 'data', None)
        return BaseHandler.fail(error_code, data)

    error_code = HTTP_EXCEPTION_ERROR_CODE_MAP.get(type(e))
    if not error_code:
        error_code = error_codes.SERVER_INTERVAL_ERROR
        error_logger.exception(e)

    return BaseHandler.fail(error_code)
