#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/11 11:54
# @Author  : xiongyaokun
# @Site    : 
# @File    : test14.py
# @Software: PyCharm

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.score = score

    @property
    def grade(self):
        if self.score >= 80:
            return 'A'
        elif 60 <= self.score < 80:
            return 'B'
        else:
            return 'C'
s = Student('xiong', 89)
print s.score
print s.grade

s.score = 101