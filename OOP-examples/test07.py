#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/10 5:29
# @Author  : xiongyaokun
# @Site    : 
# @File    : test07.py
# @Software: PyCharm

class BaseProgrammer(object):
    hobby = 'beautiful girl'
    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @classmethod
    def get_hobby(cls):
        return BaseProgrammer.hobby

    @property
    def get_weight(self):
        return self.__weight

    def self_introduction(self):
        return "My name is %s, I am %d years old." %(self.name, self._age)

class ChildProgrammer(BaseProgrammer):

    def __init__(self, name, age, weight, language):
        super(ChildProgrammer, self).__init__(name, age, weight)
        self.language = language

p = ChildProgrammer('xiongyaokun', 28, 70, 'Python')

print dir(p)
print p.__dict__
print type(p)
print isinstance(p, BaseProgrammer)
print isinstance(p, ChildProgrammer)
print isinstance(ChildProgrammer, BaseProgrammer)
print issubclass(ChildProgrammer, BaseProgrammer)
