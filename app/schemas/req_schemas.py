# -*- coding: utf-8 -*-
# created by lilei on 2019/11/27
from marshmallow import Schema, fields

from app.utils.validate_util import current_page_is_valid, page_size_is_valid


class PageListReqSchema(Schema):
    currentPage = fields.Int(required=True, default=1, validate=current_page_is_valid)  # 当前页
    pageSize = fields.Int(required=True, default=10, validate=page_size_is_valid)  # 每页大小
    keyWord = fields.Str(required=False, default='')  # 关键字
    orderBy = fields.Str(required=False, default='id')  # 排序
