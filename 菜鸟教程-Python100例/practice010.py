#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/8 22:06
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice010.py
# @Software: PyCharm
import time

print time.strftime('%Y%m%d %H%M%S', time.localtime(time.time()))

time.sleep(3)

print time.strftime('%Y%m%d %H%M%S', time.localtime(time.time()))

time.sleep(2)

print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))




