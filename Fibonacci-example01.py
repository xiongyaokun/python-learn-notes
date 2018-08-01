#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/8/11 10:26
# @Author  : xiongyaokun
# @Site    : 
# @File    : Fibonacci-example01.py
# @Software: PyCharm

class Fib(object):

    def __init__(self, num):
        a, b, lis = 0, 1, []
        for n in range(num):
            lis.append(a)
            a, b = b, a+b
        self.numbers = lis
    def __str__(self):
        return str(self.numbers)
    __repr__ = __str__

    def __len__(self):
        return len(self.numbers)

f = Fib(10)
print f
print len(f)