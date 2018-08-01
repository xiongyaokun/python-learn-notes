#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/10 14:33
# @Author  : xiongyaokun
# @Site    : 
# @File    : test11.py
# @Software: PyCharm

class Programmer(object):
    def __init__(self, name, age, language):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception("age must be int")
        self.language = language

    def __eq__(self, other):
        if isinstance(other, Programmer):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception("Must be a Programmer instance")

    def __add__(self, other):
        if isinstance(other, Programmer):
            if isinstance(other.age, int) & isinstance(self.age, int):
                return other.age + self.age
            else:
                raise Exception("age must be int type!")
        else:
            raise Exception("Must be a Programmer instance")


p1 = Programmer('Albert', 10, 'Python')
p2 = Programmer('Bob', 30, 'Java')

print p1 == p2
print p1 + p2