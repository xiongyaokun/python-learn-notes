#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/10 12:14
# @Author  : xiongyaokun
# @Site    : 
# @File    : eval-example02.py
# @Software: PyCharm

x = 1

def g():
    x = 2
    eval('x + 1')
    print 'locals():', locals()
    locals() ['x'] = 3
    print 'locals():', locals()
    print 'globals():', globals()
g()

globals() ['x'] = 5
# print 'globals():', globals()
print 'x:', x