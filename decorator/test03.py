#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/8 10:15
# @Author  : xiongyaokun
# @Site    : 
# @File    : test03.py
# @Software: PyCharm

print '**'*15, '我是分割线-简单装饰器', '**'*15
def user_logging(func):
    def wrapper():
        print "%s is running!" % func.__name__
        return func()
    return wrapper
def foo():
    print "I am a fool!"
fun = user_logging(foo)
fun()

print '**'*15, '我是分割线-语法糖装饰器-@', '**'*15

@user_logging
def bar():
    print "I am a bar!"

bar()
