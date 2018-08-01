#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/10 20:11
# @Author  : xiongyaokun
# @Site    : 
# @File    : test13.py
# @Software: PyCharm

class Programmer(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __setattr__(self, key, value):
        # setattr(self, key, value) # 错误
        self.__dict__[key] = value

    def __getattr__(self, name):
        # return getattr(self, name)
        return self.__dict__[name]
        # return super(Programmer, self).__getattr__[name]

p = Programmer('Albert', 25)
print p.name
p.language = 'Python'
print p.language