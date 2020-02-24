# -*- coding: utf-8 -*-
# created by lilei on 2019/11/5
import redis
from flask_sqlalchemy import SQLAlchemy

from app.config import env

# DB
db_url = 'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}'.format(
    pg_user=env.PG_USER,
    pg_password=env.PG_PASSWORD,
    pg_host=env.PG_HOST,
    pg_port=env.PG_PORT,
    pg_db=env.PG_DB
)
db = SQLAlchemy()
session = db.session

# Redis
_redis_pool = redis.ConnectionPool(
    host=env.REDIS_HOST,
    port=int(env.REDIS_PORT),
    password=env.REDIS_PASSWORD,
    db=int(env.REDIS_DB),
    decode_responses=True
)
redis_instance = redis.Redis(connection_pool=_redis_pool)
