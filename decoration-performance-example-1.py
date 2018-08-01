#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/5/24 9:35
# @Author  : xiongyaokun
# @Site    : 
# @File    : decoration-performance-example-1.py
# @Software: PyCharm

# decoration 装饰器，以函数作为参数，添加注释，然后再返回函数，原函数的功能不变
import time

ISOTIMEFORMAT = '%Y-%m-%d %X'
def performance(f):
    def fn(x):
        print time.strftime(ISOTIMEFORMAT, time.localtime())
        print 'call ' + f.__name__ + '()'
        return f(x)
    return fn

@performance
def factorial(n):
    return reduce(lambda x, y: x*y,range(1, n+1))
print factorial(10)