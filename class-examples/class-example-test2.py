#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/5/26 0:02
# @Author  : xiongyaokun
# @Site    : 
# @File    : class-example-test2.py
# @Software: PyCharm
class Person(object):
    def __init__(self, name, gender, birth, job):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.job = job


xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

print xiaoming.name
print xiaoming.job


class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score


p = Person('Bob', 59)

print p.name
# print p.__score
print p._Person__score
