#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/5/24 10:53
# @Author  : xiongyaokun
# @Site    : 
# @File    : decoration-performance-ex3-ultr.py
# @Software: PyCharm
import time

import functools

ISOTIMEFORMAT = '%Y-%m-%d %X'
def performance(prefix):
    def new_performance(f):
        @functools.wraps(f)
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