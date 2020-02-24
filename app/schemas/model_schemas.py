# -*- coding: utf-8 -*-
# created by lilei on 2019/11/10
from marshmallow import EXCLUDE

from app.config import ma
from app.db.models import User


class UserModelSchema(ma.ModelSchema):
    class Meta:
        model = User
        included_fk = True
        unknown = EXCLUDE
