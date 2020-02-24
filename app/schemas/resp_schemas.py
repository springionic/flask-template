# -*- coding: utf-8 -*-
# created by lilei on 2019/11/10
from marshmallow import Schema, fields


class PageListRespSchema(Schema):
    current_page = fields.Int(data_key='currentPage')
    page_size = fields.Int(data_key='pageSize')
    page_total = fields.Int(data_key='pageTotal')
    total = fields.Int()
    list = fields.Field()
