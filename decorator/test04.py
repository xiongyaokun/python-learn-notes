#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/8 10:43
# @Author  : xiongyaokun
# @Site    : 
# @File    : test04.py
# @Software: PyCharm

print "带参数的decorator-内部函数的传参"
print '**'*15, '我是分割线', '**'*15
# 定义decorator
def user_logging(func):
    def wrapper(name):
        print "%s is running!" % func.__name__
        return func(name)
    return wrapper
# 定义带装饰器的函数foo
@user_logging
def foo(name):
    print "I am %s" % name
# 调用foo
foo('xiongyaokun')

print "带参数的decorator-任意参数 *args"
print '**'*15, '我是分割线', '**'*15

def dec(func):
    def wrapper(*args):
        print "%s is running!" % func.__name__
        return func(*args)
    return wrapper

@dec
def bar(name, age, hometown):
    print "My name is %s, I am %d years old, I am from %s" %(name, age, hometown)

bar('xiongyaokun', 28, 'AnHui province')
