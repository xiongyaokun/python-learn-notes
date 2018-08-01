#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/5/24 8:37
# @Author  : xiongyaokun
# @Site    : 
# @File    : closure-example-1.py
# @Software: PyCharm

def count():
    fs = []
    for i in range(1, 4):
        def fn(j):
            def g():
                return j * j
            return g
        fs.append(fn(i))
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()