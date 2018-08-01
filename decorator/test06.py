#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/8 11:21
# @Author  : xiongyaokun
# @Site    : 
# @File    : test06.py
# @Software: PyCharm

print "带参数的decorator-向decorator传参"
print '**'*15, '我是分割线', '**'*15

def user_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == 'warn':
                print "I am warning you!"
            elif level == 'info':
                print "This is only inform you!"
            return func(*args, **kwargs)
        return wrapper
    return decorator

@user_logging(level='info')
def foo(name, age, hometown, gf_name='Zhang'):
    print "My name is %s, I am %d years old, I am from %s, My girlfriend is %s" %(name, age, hometown, gf_name)
foo('xiongyaokun', 28, 'AnHui province')

