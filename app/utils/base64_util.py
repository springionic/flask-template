# -*- coding: utf-8 -*-
# created by lilei on 2019/11/27
import binascii


def encode(text):
    return binascii.b2a_base64(text.encode(), newline=False).decode()


def decode(b64_text):
    return binascii.a2b_base64(b64_text.encode()).decode()


def is_valid_encoded_str(value: str):
    try:
        decode(value)
        return True
    except Exception:
        return False
