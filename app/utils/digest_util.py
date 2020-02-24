# -*- coding: utf-8 -*-
# created by lilei on 2019/11/27
import hashlib


def _hash_text(lib, text: str):
    func = lib()
    func.update(str(text).encode())
    return func.hexdigest()


def md5(text: str):
    return _hash_text(hashlib.md5, text)


def sha1(text: str):
    return _hash_text(hashlib.sha1, text)


def sha256(text: str):
    return _hash_text(hashlib.sha256, text)
