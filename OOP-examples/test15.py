#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/11 12:07
# @Author  : xiongyaokun
# @Site    : 
# @File    : test15.py
# @Software: PyCharm

class Person(object):
    __slots__ = ('name', 'gender')
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    __slots__ = ('name', 'gender', 'score')
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name,gender)
        self.score = score

s = Student('xiong', 'male', 59)
print s.score
s.score = 99
print s.score