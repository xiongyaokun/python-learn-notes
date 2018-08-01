#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/8 17:19
# @Author  : xiongyaokun
# @Site    : 
# @File    : test07.py
# @Software: PyCharm

from functools import wraps

print '**'*10, 'functools.wraps', '好像不用也可以的？', '**'*10

def dec(func):
    def wrapper(*args):
        print func.__name__
        print func.__doc__
        print "%s is running!" % func.__name__
        return func(*args)
    return wrapper

@dec
def bar(name, age, hometown):
    '''Some testing on bar'''
    print "My name is %s, I am %d years old, I am from %s" %(name, age, hometown)

bar('xiongyaokun', 28, 'AnHui province')
# dec(bar('xiongyaokun', 28, 'AnHui province'))


print '**'*10, '我是分割线', '**'*10

# def dec(func):
#     @wraps(func)
#     def wrapper(*args):
#         print func.__name__
#         print func.__doc__
#         print "%s is running!" % func.__name__
#         return func(*args)
#     return wrapper
#
# @dec
# def bar(name, age, hometown):
#     '''Some testing'''
#     print "My name is %s, I am %d years old, I am from %s" %(name, age, hometown)
#
# bar('xiongyaokun', 28, 'AnHui province')