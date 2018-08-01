#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/8 22:19
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice012.py
# @Software: PyCharm

"""Q:判断101-200之间有多少素数，并将素数打印出来。"""

from math import sqrt

for a in range(101, 200):
    n = 0
    temp = int(sqrt(a))
    for b in range(2, temp+1):
        if a % b == 0:
            n += 1
            break
    if n == 0:
        print a