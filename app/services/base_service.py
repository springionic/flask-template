# -*- coding: utf-8 -*-
# created by lilei on 2019/11/7
import pickle
from sqlalchemy.orm import Query

from app.db import db
from app.components.pagination import Pagination
from app.components.singleton import Singleton

IS_DELETED_COLUMN_NAME = 'delete_time'


class BaseService(object, metaclass=Singleton):

    def __init__(self):
        self.model_cls = None

    @property
    def query(self):
        return Query(self.model_cls, self.session)

    @property
    def session(self):
        session = db.session
        return session

    @property
    def redis(self):
        redis = db.redis_instance
        return redis

    def _get(self, column_name: str, value, include_deleted_item: bool = False, only_one: bool = True):
        """
        获取数据
        :param column_name: 列名称
        :param value: 列对应的检索值
        :param include_deleted_item: 是否包含已删除的项目(is_deleted = True); True: 包含; False: 不包含;
        :param only_one: 查询结果集是否仅一项; True: 仅一个符合条件的结果; False: 所有符合条件的结果;
        :return:
        """
        query = self.session.query(self.model_cls).filter(getattr(self.model_cls, column_name) == value)
        # 如果有 is_deleted 列
        if hasattr(self.model_cls, IS_DELETED_COLUMN_NAME) and not include_deleted_item:
            query = query.filter_by(delete_time=None)
        return query.first() if only_one else query.all()

    def get(self, column_name: str, value, include_deleted_item: bool = False):
        return self._get(column_name, value, include_deleted_item)

    def get_by_id(self, value: int, include_deleted_item: bool = False):
        return self.get('id', value, include_deleted_item)

    def list(self, column_name: str, value, include_deleted_item: bool = False):
        return self._get(column_name, value, include_deleted_item, only_one=False)

    def list_all(self):
        return self.session.query(self.model_cls).all()

    def list_pagination(self, current_page, page_size, filters, order_bys, include_deleted_item: bool = False):
        if not filters:
            filters = []

        if not include_deleted_item:
            filters.append(self.model_cls.delete_time.is_(None))

        current_page = int(current_page)
        page_size = int(page_size)
        items = self.session.query(self.model_cls) \
            .filter(*filters) \
            .order_by(*order_bys) \
            .limit(page_size) \
            .offset((current_page - 1) * page_size) \
            .all()

        if current_page == 1 and len(items) < page_size:
            total = len(items)
        else:
            total = self.session.query(self.model_cls).filter(*filters).order_by(*order_bys).count()

        return Pagination(current_page, page_size, total, items)

    def add(self, instance):
        session = self.session
        session.add(instance)
        session.commit()
        session.refresh(instance)
        return instance

    def update(self, instance):
        session = self.session
        instance = session.merge(instance)
        session.commit()
        session.refresh(instance)
        return instance

    def cache_set_obj(self, key, obj, ex=None):
        self.redis.set(key, pickle.dumps(obj), ex=ex)

    def cache_get_obj(self, key):
        value = self.redis.get(key)
        if not value:
            return None
        return pickle.loads(value)
