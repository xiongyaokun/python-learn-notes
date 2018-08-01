#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/10 22:54
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice019.py
# @Software: PyCharm

"""
Q:一个数如果恰好等于它的因子之和，这个数就称为"完数"。
例如6=1＋2＋3.编程找出1000以内的所有完数。
"""

for a in range(1, 10):
    temp = []
    for i in range(1, a+1):
        while a % i == 0:
            temp.append(i)
            a = a / i
            if a == 1:
                break
    # print temp
    if a == sum(temp):
        print "%d =" % a, '+'.join(map(lambda x : str(x), temp))