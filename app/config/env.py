# -*- coding: utf-8 -*-
# created by lilei on 2019/11/5
import json
import os


BASE_DIR = os.path.dirname(os.path.abspath(__name__))

env = os.getenv('ENV', 'dev')  # dev, test, master

_env_dict = dict()
_json_dir = os.path.join(BASE_DIR, 'app', 'config', 'env_json')
_suffix = '.json'

with open(os.path.join(_json_dir, env + _suffix), 'r') as f:
    env_content = f.read()

env_dict = json.loads(env_content)
for k, v in env_dict:
    _env_dict[k] = v

# PostgreSQL
PG_HOST = _env_dict.get('PG_HOST', '127.0.0.1')
PG_PORT = _env_dict.get('PG_PORT', 5432)
PG_DB = _env_dict.get('PG_DB', 'flask')
PG_USER = _env_dict.get('PG_USER', 'postgres')
PG_PASSWORD = _env_dict.get('PG_PASSWORD', 'lilei120400')

# Redis
REDIS_HOST = _env_dict.get('REDIS_HOST', '127.0.0.1')
REDIS_PORT = _env_dict.get('REDIS_PORT', 3306)
REDIS_DB = _env_dict.get('REDIS_DB', 1)
REDIS_PASSWORD = _env_dict.get('REDIS_PASSWORD', 'flask')

DEBUG_STATUS = _env_dict.get('DEBUG', True)
