#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/10 4:45
# @Author  : xiongyaokun
# @Site    : 
# @File    : test05.py
# @Software: PyCharm

class Programmer(object):
    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        return self.__weight

p = Programmer('xiongyaokun', 28, 70)

print dir(p)
print p.__dict__
print p.get_weight()
print p._Programmer__weight


