#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/10 19:56
# @Author  : xiongyaokun
# @Site    : 
# @File    : test12.py
# @Software: PyCharm

print "重写__str__, __repr__, __unicode__方法"

class Programmer(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "My name is %s" % self.name

    def __repr__(self):
        return "My age is %s" % self.age

    def __unicode__(self):
        return "My name is %s, I am %d years old." %(self.name, self.age)


class NewProgrammer(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Programmer('xiong', 28)
print p1.__str__()
print p1
print p1.__repr__()
print p1.__unicode__()
p2 = NewProgrammer('xiong', 28)
print p2
print p2.__str__()
print p2.__repr__()
# print p2.__unicode__()
