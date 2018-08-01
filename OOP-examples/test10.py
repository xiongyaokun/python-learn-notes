#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/10 13:19
# @Author  : xiongyaokun
# @Site    : 
# @File    : test10.py
# @Software: PyCharm

class Programmer(object):
    def __new__(cls, *args, **kwargs):
        print "call __new__ method"
        print args
        return super(Programmer, cls).__new__(cls, *args, **kwargs)

    def __init__(self, name, age):
        print "call __init__ method"
        self.name = name
        self.age = age

p = Programmer('xiong', 28)
print p.__dict__