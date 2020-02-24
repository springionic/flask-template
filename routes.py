# -*- coding: utf-8 -*-
# created by lilei on 2019/11/8

from flask import Blueprint

from app.handlers.user_handler import *


bp_user = Blueprint('user', __name__, url_prefix='/api/user')
bp_user.add_url_rule('/add/', view_func=UserAddHandler.as_view('user_add'))
bp_user.add_url_rule('/delete/', view_func=UserDelHandler.as_view('user_delete'))
bp_user.add_url_rule('/update/', view_func=UserDelHandler.as_view('user_update'))
bp_user.add_url_rule('/single/', view_func=UserSingleHandler.as_view('user_single'))
bp_user.add_url_rule('/list/', view_func=UserListHandler.as_view('user_list'))



# blueprint list
bp_list = [
    bp_user
]
