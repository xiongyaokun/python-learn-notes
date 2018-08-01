#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/8 11:12
# @Author  : xiongyaokun
# @Site    : 
# @File    : test05.py
# @Software: PyCharm

print "带参数的decorator-关键字参数 **kwargs"
print '**'*15, '我是分割线', '**'*15

def dec(func):
    def wrapper(*args, **kwargs):
        print "%s is running!" % func.__name__
        return func(*args, **kwargs)
    return wrapper

@dec
def bar(name, age, hometown, gf_name='Zhang'):
    print "My name is %s, I am %d years old, I am from %s, my girlfriend name is %s" %(name, age, hometown, gf_name)

bar('xiongyaokun', 28, 'AnHui province')