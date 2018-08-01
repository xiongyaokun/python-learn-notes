#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/8 20:17
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice007.py
# @Software: PyCharm

"""Q：将一个列表的数据复制到另一个列表中"""
a = [1, 2, 3, 4, 5]
b= a[:]
print b

import copy
c = copy.copy(a)
print c

