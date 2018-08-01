#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/10 12:44
# @Author  : xiongyaokun
# @Site    : 
# @File    : test08.py
# @Software: PyCharm


class A(object):
    def __init__(self, a):
        print a
        self.s = str(a)

    def a_method(self):
        print "I have a string %s" %self.s

class B(object):
    def __init__(self, a, b):
        print a+b
        self.st = str(a) + str(b)

    def b_method(self):
        print "I have a string %s" %self.st

class C(A, B):
    def __init__(self, a, b, c):
        super(C, self).__init__(a)
        B.__init__(self, b, c)

c = C(1, 2, 3)
c.a_method()
c.b_method()
