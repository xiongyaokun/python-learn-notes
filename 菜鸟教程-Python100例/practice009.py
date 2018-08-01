#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/8 20:55
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice009.py
# @Software: PyCharm


"""Q:暂停一秒输出."""

import time

a = {'first_name': 'xiong', 'last_name': 'yaokun', 'age': 28}
for key, value in a.items():
    print key, value
    time.sleep(1)