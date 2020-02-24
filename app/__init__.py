# -*- coding: utf-8 -*-
# created by lilei at 2020/2/24

from flask import Flask

from app.components.error_handler import handler_error
from app.config import Config, ma, mail
from app.db import db as app_db
from middlewares import before_request_funcs, after_request_funcs
from routes import bp_list


def create_app() -> Flask:
    """返回app对象"""
    app = Flask(__name__, template_folder=None, static_folder=None)
    # 配置app
    app.config.from_object(Config)
    # 初始化扩展插件
    app_db.init_app(app)
    ma.init_app(app)
    # search.init_app(app)
    mail.init_app(app)

    # 中间件
    pb_before_request_funcs_map = {}
    pb_after_request_funcs_map = {}
    for bp in bp_list:
        pb_before_request_funcs_map[bp.name] = before_request_funcs
        pb_after_request_funcs_map[bp.name] = after_request_funcs
    app.before_request_funcs = pb_before_request_funcs_map
    app.after_request_funcs = pb_after_request_funcs_map

    for bp in bp_list:  # 注册蓝图
        app.register_blueprint(bp)

    app.register_error_handler(Exception, handler_error)  # 注册异常处理


    return app
