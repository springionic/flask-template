# -*- coding: utf-8 -*-
# created by lilei on 2019/11/27
from datetime import datetime


def datetime_to_timestamp(datetime_instance):
    """
    datetime 转换为 timestamp
    :param datetime_instance:
    :return:
    """
    return int(datetime_instance.timestamp())


def datetime_to_timestamp_ms(datetime_instance):
    """
    datetime 转换为 timestamp (毫秒)
    :param datetime_instance:
    :return:
    """
    return int(datetime_instance.timestamp() * 1000)


def timestamp_to_datetime(timestamp):
    """
    timestamp 转换为 datetime
    :param timestamp:
    :return:
    """
    return datetime.fromtimestamp(timestamp)


def timestamp_ms_to_datetime(timestamp):
    """
    timestamp (毫秒) 转换为 datetime
    :param timestamp:
    :return:
    """
    return datetime.fromtimestamp(timestamp / 1000)


def now_datetime():
    """
    获取当前 datetime
    :return:
    """
    return datetime.now()


def now_timestamp():
    """
    获取当前 timestamp
    :return:
    """
    return datetime_to_timestamp(now_datetime())


def now_timestamp_ms():
    """
    获取当前 timestamp (毫秒)
    :return:
    """
    return datetime_to_timestamp_ms(now_datetime())


def today_datetime():
    """
    获取今天 0 时 0 分 0 秒 datetime
    :return:
    """
    today = datetime.today()
    return datetime(year=today.year, month=today.month, day=today.day)


def today_timestamp():
    """
    获取今天 0 时 0 分 0 秒 timestamp
    :return:
    """
    return datetime_to_timestamp(today_datetime())


def today_timestamp_ms():
    """
    获取今天 0 时 0 分 0 秒 timestamp (毫秒)
    :return:
    """
    return datetime_to_timestamp_ms(today_datetime())


def str_to_datetime(date_str, format_str='%Y-%m-%d %H:%M:%S'):
    """
    timestamp 转换为 datetime
    :param date_str:
    :param format_str:
    :return:
    """
    return datetime.strptime(date_str, format_str)


def datetime_to_str(datetime_instance, format_str='%Y-%m-%d %H:%M:%S'):
    """
    datetime 转换为 timestamp
    :param datetime_instance:
    :param format_str:
    :return:
    """
    return datetime.strftime(datetime_instance, format_str)
