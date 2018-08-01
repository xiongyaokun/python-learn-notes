#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/8 23:00
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice013.py
# @Software: PyCharm

"""Q:打印100～999之间的水仙花数，水仙花数是指，其各位数的立方根之和等于该数。"""

"""方法一："""
# for a in range(100, 1000):
#     i = a % 10
#     j = (a / 10) % 10
#     k = a / 100
#     # if a == i*i*i + j*j*j + k*k*k:
#     if a == i **3 + j ** 3 + k ** 3:
#         print a


"""方法二："""
# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             a = i*100 + j*10 + k
#             b = i**3 + j**3 + k**3
#             if a == b and a > 100:
#                 print a

"""方法三："""
for a in range(100, 1000):
    b = str(a)
    c = map(lambda x : int(x)**3, b)
    if sum(c) == a:
        print sum(c)