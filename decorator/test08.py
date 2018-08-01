#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/8 17:46
# @Author  : xiongyaokun
# @Site    : 
# @File    : test08.py
# @Software: PyCharm

print '**'*10, '类装饰器', '**'*10
print "使用类装饰器主要依靠类的__call__方法，当使用@形式将装饰器附加到函数上时，就会调用此方法。"

class Foo(object):
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print "class decorator running"
        self.func()
        print "class decorator ending"

@Foo
def bar():
    print "This is bar running!"

bar()