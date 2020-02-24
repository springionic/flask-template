# -*- coding: utf-8 -*-
# created by lilei at 2020/2/24
from app.config import error_codes
from app.config.exceptions import BusinessException
from app.db.models import User
from app.services.base_service import BaseService


class UserService(BaseService):

    def __init__(self):
        super(UserService, self).__init__()
        self.model_cls = User

    def update_user(self, id, user_data: dict):
        user = self.get_by_id(id)
        if not user:
            raise BusinessException(error_codes.USER_NOT_FOUND)
        for k, v in user_data.items():
            setattr(user, k, v)
        return self.update(user)