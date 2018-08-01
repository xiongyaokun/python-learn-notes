#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/7 23:30
# @Author  : xiongyaokun
# @Site    : 
# @File    : test02.py
# @Software: PyCharm

def foo():
    print 'foo!'

def bar(func):
    func()

bar(foo)
print "**"*15, '我是分割线', '**'*15


def dec(func):
    print "I am decorating!"
    return func
@dec
def test_func():
    print "I am testing decorating!"

test_func()

print "**"*15, '我是分割线', '**'*15

def user_logging(func):
    print "I am user_logging!"
    print "%s is runnging." %(func.__name__)
    return func()
user_logging(test_func)

print "**"*15, '我是分割线', '**'*15
