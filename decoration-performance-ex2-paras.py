#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/5/24 10:11
# @Author  : xiongyaokun
# @Site    : 
# @File    : decoration-performance-ex2-paras.py
# @Software: PyCharm

# 带参数的装饰器，和无参数的装饰器比较，又多嵌套了一层函数，最外层decoration函数负责传入可变参数
import time

ISOTIMEFORMAT = '%y-%m-%d %X'
def performance(prefix):
    def new_performance(f):
        def fn(*args, **kwargs):
            print '[%s] %s' % (prefix, f.__name__)
            print time.strftime(ISOTIMEFORMAT, time.localtime())
            print 'call ' + f.__name__ + '()'
            return f(*args, **kwargs)
        return fn
    return new_performance

@performance('DEBUG')
def factorial(n):
    return reduce(lambda x, y: x*y,range(1, n+1))
print factorial(10)