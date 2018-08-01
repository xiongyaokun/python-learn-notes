#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/10 13:04
# @Author  : xiongyaokun
# @Site    : 
# @File    : test09.py
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
    def self_introduction(self):
        return "My name is %s, my favourite language is %s." %(self.name, self.language)

def introduce(p):
    if isinstance(p, BaseProgrammer):
        print p.self_introduction()


p = ChildProgrammer('xiongyaokun', 28, 70, 'Python')
p1 = BaseProgrammer('xiong', 28, 70)
introduce(p)
introduce(p1)
