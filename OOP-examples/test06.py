#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/10 5:07
# @Author  : xiongyaokun
# @Site    : 
# @File    : test06.py
# @Software: PyCharm

class Programmer(object):

    hobby = 'beautiful girl'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @classmethod
    def get_hobby(cls):
        return Programmer.hobby

    @property
    def get_weight(self):
        return self.__weight

    def self_introduction(self):
        return "My name is %s, I am %d years old." %(self.name, self._age)

p = Programmer('xiong', 28, 70)

print dir(p)
print '**'*10, '我是分割线', '**'*10
print p.get_hobby()
print Programmer.get_hobby()
print Programmer.hobby

print p.get_weight
print p.self_introduction()