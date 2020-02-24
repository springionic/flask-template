# -*- coding: utf-8 -*-
# created by lilei on 2019/12/25
import typing


def to_str_list(data: typing.Iterable):
    return [str(item) for item in data]


def to_str_set(data: typing.Iterable):
    return set(to_str_list(data))


def split_by_comma(value: str):
    if not value:
        return []
    return value.split(',')


def split_by_dot(value: str):
    if not value:
        return []
    return value.split('.')


def to_comma_split_str(data: typing.Iterable):
    return ','.join(to_str_list(data))
