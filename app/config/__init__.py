# -*- coding: utf-8 -*-
# created by lilei on 2019/11/5
from flask_mail import Mail
from flask_marshmallow import Marshmallow

from app.config.env import DEBUG_STATUS
from app.db import db_url, db


class Config:
    DEBUG = DEBUG_STATUS
    SQLALCHEMY_DATABASE_URI = db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    WHOOSH_BASE = 'whoosh_index'
    WHOOSH_ENABLE = True


ma = Marshmallow()  # 序列化
mail = Mail()  # 邮件扩展
