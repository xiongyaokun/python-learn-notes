#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/10 4:26
# @Author  : xiongyaokun
# @Site    : 
# @File    : test04.py
# @Software: PyCharm

print '**'*10, 'old-style', '**'*10

class Oldstyle():

    def __init__(self, name, age):
        self.name = name
        self.age = age

old = Oldstyle('xiong', 28)
print old
print type(old)
print dir(old)

print '**'*10, '我是分割线', '**'*10
print '**'*10, 'old-style', '**'*10

class Newstyle(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

new = Newstyle('yaokun', 28)
print new
print type(new)
print dir(new)
